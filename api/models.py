import sys
from datetime import datetime
from io import BytesIO
from urllib.parse import urlparse
from uuid import uuid4

from django.core.exceptions import ValidationError
from django.core.files import File
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models
from django.utils.dateparse import parse_datetime
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
    return "team/{}-{}.{}".format(instance.name, uuid4().hex, ext)


def team_webp_upload(instance, filename):
    ext = filename.split(".")[-1]
    return "team/webp/{}-{}.{}".format(instance.name, uuid4().hex, ext)


def workshop_upload(instance, filename):
    ext = filename.split(".")[-1]
    return "workshop/{}/{}-{}.{}".format(
        instance.event_date.year, instance.title, uuid4().hex, ext
    )


def workshop_webp_upload(instance, filename):
    ext = filename.split(".")[-1]
    return "workshop/{}/webp/{}-{}.{}".format(
        instance.event_date.year, instance.title, uuid4().hex, ext
    )


def gallery_upload(instance, filename):
    ext = filename.split(".")[-1]
    return "gallery/{}/{}/{}/{}.{}".format(
        instance.year, instance.event, instance.sub_event, uuid4().hex, ext
    )


def thumbnail_upload(instance, filename):
    ext = filename.split(".")[-1]
    return "thumbnail/{}/{}/{}/{}.{}".format(
        instance.year, instance.event, instance.sub_event, uuid4().hex, ext
    )


def alumni_upload(instance, filename):
    ext = filename.split(".")[-1]
    return "alumni/{}/{}-{}.{}".format(instance.batch, instance.name, uuid4().hex, ext)


def alumni_webp_upload(instance, filename):
    ext = filename.split(".")[-1]
    return "alumni/{}/webp/{}-{}.{}".format(
        instance.batch, instance.name, uuid4().hex, ext
    )


def project_upload(instance, filename):
    ext = filename.split(".")[-1]
    return "projects/{}/{}/{}-{}.{}".format(
        instance.domain, instance.year, instance.name, uuid4().hex, ext
    )


def project_webp_upload(instance, filename):
    ext = filename.split(".")[-1]
    return "projects/{}/{}/webp/{}-{}.{}".format(
        instance.domain, instance.year, instance.name, uuid4().hex, ext
    )


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


def generate_webp(image, quality=80):
    output = BytesIO()
    image.save(output, format="WEBP", quality=quality)
    output.seek(0)
    return InMemoryUploadedFile(
        output,
        "ImageField",
        "image.webp",
        "image/webp",
        sys.getsizeof(output),
        None,
    )


class ResizeImageMixin:
    def resize(self, imageField: models.ImageField, size: tuple, name, format):
        image = Image.open(imageField)
        image = image.convert("RGB")
        height_percent = size / image.height
        width_size = int((image.width) * (height_percent))
        thumbnail = image.resize((width_size, size))
        output = BytesIO()
        thumbnail.save(output, format=format)
        output.seek(0)

        content_file = ContentFile(output.read())
        file = File(content_file)

        imageField.save(name, file, save=False)


class AccessModel(models.Model):
    time = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        AccessModel.objects.all().delete()
        super(AccessModel, self).save(*args, **kwargs)


class TeamModel(models.Model, ResizeImageMixin):
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
    profile_pic_webp = models.ImageField(
        upload_to=team_webp_upload, null=True, blank=True
    )
    profile_pic_url = models.URLField(max_length=500, null=True, blank=True)
    profile_pic_webp_url = models.URLField(max_length=500, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Team Members"

    def save(self, *args, **kwargs):

        if self.profile_pic and self.pk is None:
            self.profile_pic_webp = generate_webp(Image.open(self.profile_pic))
            self.resize(self.profile_pic, 512, "image.jpeg", "jpeg")
            self.resize(self.profile_pic_webp, 512, "image.webp", "webp")

        super(TeamModel, self).save(*args, **kwargs)

    def update_team_image_url(self):
        if self.profile_pic:
            self.profile_pic_url = self.profile_pic.url
            self.profile_pic_webp_url = self.profile_pic_webp.url
            self.save()

    def __str__(self):
        return self.name


class Workshop(models.Model, ResizeImageMixin):
    title = models.CharField(max_length=500)
    description = models.TextField()
    event_date = models.DateTimeField()
    venue = models.CharField(max_length=100)
    cover = models.ImageField(upload_to=workshop_upload, null=True, blank=True)
    cover_webp = models.ImageField(
        upload_to=workshop_webp_upload, null=True, blank=True
    )
    cover_url = models.URLField(max_length=500, null=True, blank=True)
    cover_webp_url = models.URLField(max_length=500, null=True, blank=True)

    def save(self, *args, **kwargs):

        if self.cover and self.pk is None:
            self.cover_webp = generate_webp(Image.open(self.cover))
            self.resize(self.cover, 512, "image.jpeg", "jpeg")
            self.resize(self.cover_webp, 512, "image.webp", "webp")

        super(Workshop, self).save(*args, **kwargs)

    def update_workshop_cover_url(self):
        if self.cover:
            self.cover_url = self.cover.url
            self.cover_webp_url = self.cover_webp.url
            self.save()

    def __str__(self):
        return self.title


class Gallery(models.Model, ResizeImageMixin):
    event = models.CharField(max_length=50, null=False, default=None)
    sub_event = models.CharField(max_length=100, null=False, default=None)
    year = models.PositiveIntegerField()
    image = models.ImageField(upload_to=gallery_upload, null=True, blank=True)
    thumb_image = models.ImageField(upload_to=thumbnail_upload, null=True, blank=True)
    image_url = models.URLField(max_length=500, null=True, blank=True)
    thumb_image_url = models.URLField(max_length=500, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Gallery"

    def save(self, *args, **kwargs):

        if self.image and self.pk is None:
            self.thumb_image = generate_webp(Image.open(self.image))
            self.resize(self.thumb_image, 512, "image.webp", "webp")

        super(Gallery, self).save(*args, **kwargs)

    def update_gallery_image_url(self):
        if self.image:
            self.image_url = self.image.url
            self.thumb_image_url = self.thumb_image.url
            self.save()

    def __str__(self):
        return self.event


class Alumni(models.Model, ResizeImageMixin):
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
    profile_pic_webp = models.ImageField(
        upload_to=alumni_webp_upload, null=True, blank=True
    )
    profile_pic_url = models.URLField(max_length=500, null=True, blank=True)
    profile_pic_webp_url = models.URLField(max_length=500, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Alumni"

    def save(self, *args, **kwargs):

        if self.profile_pic and self.pk is None:
            self.profile_pic_webp = generate_webp(Image.open(self.profile_pic))
            self.resize(self.profile_pic, 512, "image.jpeg", "jpeg")
            self.resize(self.profile_pic_webp, 512, "image.webp", "webp")

        super(Alumni, self).save(*args, **kwargs)

    def update_alumni_image_url(self):
        if self.profile_pic:
            self.profile_pic_url = self.profile_pic.url
            self.profile_pic_webp_url = self.profile_pic_webp.url
            self.save()

    def __str__(self):
        return self.name


class Project(models.Model, ResizeImageMixin):
    domain = models.CharField(max_length=50, null=False, default=None)
    name = models.CharField(max_length=50, null=False, default=None)
    description = models.TextField()
    year = models.PositiveIntegerField()
    github_link = models.URLField(
        max_length=100, null=True, blank=True, validators=[validate_github_url]
    )
    cover = models.ImageField(upload_to=project_upload, null=True, blank=True)
    cover_webp = models.ImageField(upload_to=project_webp_upload, null=True, blank=True)
    cover_url = models.URLField(max_length=500, null=True, blank=True)
    cover_webp_url = models.URLField(max_length=500, null=True, blank=True)

    def save(self, *args, **kwargs):

        if self.cover and self.pk is None:
            self.cover_webp = generate_webp(Image.open(self.cover))
            self.resize(self.cover, 512, "image.jpeg", "jpeg")
            self.resize(self.cover_webp, 512, "image.webp", "webp")

        super(Project, self).save(*args, **kwargs)

    def update_project_cover_url(self):
        if self.cover:
            self.cover_url = self.cover.url
            self.cover_webp_url = self.cover_webp.url
            self.save()

    def __str__(self):
        return self.name
