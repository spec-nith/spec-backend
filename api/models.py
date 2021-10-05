from urllib.parse import urlparse
from uuid import uuid4

from django.core.exceptions import ValidationError
from django.db import models

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


def blog_upload(instance, filename):
    ext = filename.split(".")[-1]
    return "blogs/{}.{}".format(uuid4().hex, ext)


def workshop_upload(instance, filename):
    ext = filename.split(".")[-1]
    return "workshop/{}.{}".format(uuid4().hex, ext)


def gallery_upload(instance, filename):
    ext = filename.split(".")[-1]
    return "gallery/{}.{}".format(uuid4().hex, ext)


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
    description = models.TextField(null=True, blank=True)
    github_id = models.URLField(
        max_length=100, null=True, blank=True, validators=[validate_github_url]
    )
    linkedin_id = models.URLField(
        max_length=100, null=True, blank=True, validators=[validate_linkedin_url]
    )
    profile_pic = models.ImageField(upload_to=team_upload, null=True, blank=True)
    profile_pic_url = models.URLField(max_length=500, null=True, blank=True)

    def update_team_image_url(self):
        if self.profile_pic:
            self.profile_pic_url = self.profile_pic.url
            self.save()

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    author = models.CharField(max_length=50)
    body = models.JSONField()
    published = models.DateField(auto_now_add=True)
    cover = models.ImageField(upload_to=blog_upload, null=True, blank=True)
    cover_url = models.URLField(max_length=500, null=True, blank=True)

    def update_blog_cover_url(self):
        if self.cover:
            self.cover_url = self.cover.url
            self.save()

    def __str__(self):
        return self.title


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
    image_url = models.URLField(max_length=500, null=True, blank=True)

    def update_gallery_image_url(self):
        if self.image:
            self.image_url = self.image.url
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
