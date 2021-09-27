from django.db import models


class TeamModel(models.Model):
    name = models.CharField(max_length=50, null=False, default=None)
    year = models.IntegerField()
    # choices in charfield #validators
    title = models.CharField(max_length=50, null=False, default=None)
    github_id = models.URLField(max_length=100, null=True, blank=True)
    linkedin_id = models.URLField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    author = models.CharField(max_length=50)
    body = models.JSONField()
    published = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Workshop(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    event_date = models.DateTimeField()
    venue = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Alumni(models.Model):
    name = models.CharField(max_length=50, null=False, default=None)
    year = models.IntegerField()
    # choices in charfield #validators
    title = models.CharField(max_length=50, null=False, default=None)
    github_id = models.URLField(max_length=100, null=True, blank=True)
    linkedin_id = models.URLField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name
