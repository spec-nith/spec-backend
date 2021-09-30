from urllib.parse import urlparse
from uuid import uuid4

from django.core.exceptions import ValidationError

# from api.views import save
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


def validate_github_url(value):
    if not value:
        return  # Required error is done the field
    obj = urlparse(value)
    if not obj.hostname in ("github.com"):
        raise ValidationError(f"Only URLs from GitHub are allowed")


def validate_linkedin_url(value):
    if not value:
        return  # Required error is done the field
    obj = urlparse(value)
    if not obj.hostname in ("linkedin.com", "www.linkedin.com", "linkedin.in"):
        raise ValidationError(f"Only URLs from GitHub are allowed")


class TeamModel(models.Model):
    name = models.CharField(max_length=50, null=False, default=None)
    # choices in charfield #validators
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

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=2000)
    author = models.CharField(max_length=50)
    body = models.JSONField()
    published = models.DateField(auto_now_add=True)
    cover = models.ImageField(upload_to=blog_upload, null=True, blank=True)

    def __str__(self):
        return self.title


class Workshop(models.Model):
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=2000)
    event_date = models.DateTimeField()
    venue = models.CharField(max_length=100)
    cover = models.ImageField(upload_to=workshop_upload, null=True, blank=True)

    def __str__(self):
        return self.title


class Gallery(models.Model):
    event = models.CharField(max_length=50, null=False, default=None)
    date = models.DateField()
    sub_event = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to=gallery_upload, null=True, blank=True)

    def __str__(self):
        return self.event


class Alumni(models.Model):
    name = models.CharField(max_length=50, null=False, default=None)
    year = models.IntegerField()
    dual_degree = models.BooleanField(default=False)
    # choices in charfield #validators
    company = models.CharField(max_length=100, null=False, default=None)
    github_id = models.URLField(
        max_length=100, null=True, blank=True, validators=[validate_github_url]
    )
    linkedin_id = models.URLField(
        max_length=100, null=True, blank=True, validators=[validate_linkedin_url]
    )
    profile_pic = models.ImageField(upload_to=alumni_upload, null=True, blank=True)

    def __str__(self):
        return self.name
