import sys
from io import BytesIO
from urllib.parse import urlparse
from uuid import uuid4

from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models
from PIL import Image

CHOICES = (
    ("Volunteer", "Volunteer"),
    ("Executive", "Executive"),
    ("Coordinator", "Coordinator"),
    ("President", "President"),
    ("Vice President", " Vice President"),
    ("Technical Lead", "Technical Lead"),
    ("Finance Head", "Finance Head"),
    ("Web Development Head", "Web Development Head"),
    ("Public Relation Head", "Public Relation Head"),
)


def team_upload(instance, filename):
    ext = filename.split(".")[-1]
    return "team/{}.{}".format(uuid4().hex, ext)


def workshop_upload(instance, filename):
    ext = filename.split(".")[-1]
    return "workshop/{}.{}".format(uuid4().hex, ext)


def gallery_upload(instance, filename):
    ext = filename.split(".")[-1]
    return "gallery/{}.{}".format(uuid4().hex, ext)


def thumbnail_upload(instance, filename):
    ext = filename.split(".")[-1]
    return "thumbnail/{}.{}".format(uuid4().hex, ext)


def alumni_upload(instance, filename):
    ext = filename.split(".")[-1]
    return "alumni/{}.{}".format(uuid4().hex, ext)


def project_upload(instance, filename):
    ext = filename.split(".")[-1]
    return "projects/{}.{}".format(uuid4().hex, ext)


def validate_github_url(value):
    if not value:
        return
    obj = urlparse(value)
    if not obj.hostname in ("github.com"):
        raise ValidationError(f"Only URLs from GitHub are allowed")


def validate_linkedin_url(value):
    if not value:
        return
    obj = urlparse(value)
    if not obj.hostname in ("linkedin.com", "www.linkedin.com", "linkedin.in"):
        raise ValidationError(f"Only URLs from Linkedin are allowed")


class AccessModel(models.Model):
    time = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        AccessModel.objects.all().delete()
        super(AccessModel, self).save(*args, **kwargs)


class TeamModel(models.Model):
    name = models.CharField(max_length=50, null=False, default=None)
    title = models.CharField(
        max_length=50, choices=CHOICES, null=False, default="Volunteer"
    )
    github_id = models.URLField(
        max_length=100, null=True, blank=True, validators=[validate_github_url]
    )
    linkedin_id = models.URLField(
        max_length=100, null=True, blank=True, validators=[validate_linkedin_url]
    )
    profile_pic = models.ImageField(upload_to=team_upload, null=True, blank=True)
    profile_pic_url = models.URLField(max_length=500, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Team Members"

    def update_team_image_url(self):
        if self.profile_pic:
            self.profile_pic_url = self.profile_pic.url
            self.save()

    def __str__(self):
        return self.name


class Workshop(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    event_date = models.DateTimeField()
    venue = models.CharField(max_length=100)
    cover = models.ImageField(upload_to=workshop_upload, null=True, blank=True)
    cover_url = models.URLField(max_length=500, null=True, blank=True)

    def update_workshop_cover_url(self):
        if self.cover:
            self.cover_url = self.cover.url
            self.save()

    def __str__(self):
        return self.title


class Gallery(models.Model):
    event = models.CharField(max_length=50, null=False, default=None)
    sub_event = models.CharField(max_length=100, blank=True, null=True)
    year = models.PositiveIntegerField(null=True, blank=True)
    image = models.ImageField(upload_to=gallery_upload, null=True, blank=True)
    thumb_image = models.ImageField(upload_to=thumbnail_upload, null=True, blank=True)
    image_url = models.URLField(max_length=500, null=True, blank=True)
    thumb_image_url = models.URLField(max_length=500, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.image and self.pk is None:
            imageTemp = Image.open(self.image)
            imageTemp = imageTemp.convert("RGB")
            output = BytesIO()
            THUMB_SIZE = [512, 256]
            if imageTemp.height > imageTemp.width and imageTemp.height > 512:
                height_percent = THUMB_SIZE[0] / float(imageTemp.height)
                width_size = int((float(imageTemp.width) * float(height_percent)))
                imageTempResized = imageTemp.resize((width_size, THUMB_SIZE[0]))
            elif imageTemp.height <= imageTemp.width and imageTemp.width > 512:
                width_percent = THUMB_SIZE[0] / float(imageTemp.width)
                height_size = int((float(imageTemp.height) * float(width_percent)))
                imageTempResized = imageTemp.resize((THUMB_SIZE[0], height_size))

            imageTempResized.save(output, format="WEBP", quality=92)
            output.seek(0)
            self.thumb_image = InMemoryUploadedFile(
                output,
                "ImageField",
                "image.webp",
                "image/webp",
                sys.getsizeof(output),
                None,
            )
        super(Gallery, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Gallery"

    def update_gallery_image_url(self):
        if self.image:
            self.image_url = self.image.url
            self.thumb_image_url = self.thumb_image.url
            self.save()

    def __str__(self):
        return self.event


class Alumni(models.Model):
    name = models.CharField(max_length=50, null=False, default=None)
    batch = models.PositiveIntegerField(null=True, blank=True)
    dual_degree = models.BooleanField(default=False)
    company = models.CharField(max_length=100, null=False, default=None)
    github_id = models.URLField(
        max_length=100, null=True, blank=True, validators=[validate_github_url]
    )
    linkedin_id = models.URLField(
        max_length=100, null=True, blank=True, validators=[validate_linkedin_url]
    )
    profile_pic = models.ImageField(upload_to=alumni_upload, null=True, blank=True)
    profile_pic_url = models.URLField(max_length=500, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Alumni"

    def update_alumni_image_url(self):
        if self.profile_pic:
            self.profile_pic_url = self.profile_pic.url
            self.save()

    def __str__(self):
        return self.name


class Project(models.Model):
    domain = models.CharField(max_length=50, null=False, default=None)
    name = models.CharField(max_length=50, null=False, default=None)
    description = models.TextField()
    year = models.PositiveIntegerField(null=True, blank=True)
    github_link = models.URLField(
        max_length=100, null=True, blank=True, validators=[validate_github_url]
    )
    cover = models.ImageField(upload_to=project_upload, null=True, blank=True)
    cover_url = models.URLField(max_length=500, null=True, blank=True)

    def update_project_cover_url(self):
        if self.cover:
            self.cover_url = self.cover.url
            self.save()

    def __str__(self):
        return self.name
