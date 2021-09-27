from django.db import models


class TeamModel(models.Model):
    name = models.CharField(max_length=50, null=False, default=None)
    # choices in charfield #validators
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
    title = models.CharField(
        max_length=50, choices=CHOICES, null=False, default="Volunteer"
    )
    github_id = models.URLField(max_length=100, null=True, blank=True)
    linkedin_id = models.URLField(max_length=100, null=True, blank=True)
    image = models.URLField(
        default="http://uilove.in/realestate/listo/preview/img/profile-placeholder.jpg"
    )

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=2000)
    author = models.CharField(max_length=50)
    body = models.JSONField()
    published = models.DateField(auto_now_add=True)
    image = models.URLField(
        default="https://assets.thehansindia.com/h-upload/2021/07/31/1092805-tech.webp"
    )

    def __str__(self):
        return self.title


class Workshop(models.Model):
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=2000)
    event_date = models.DateTimeField()
    venue = models.CharField(max_length=100)
    image = models.URLField(
        max_length=300,
        default="https://s3.amazonaws.com/thumbnails.venngage.com/template/93542d3a-62a9-4674-a7ed-cb6852d160a3.png",
    )

    def __str__(self):
        return self.title


class Alumni(models.Model):
    name = models.CharField(max_length=50, null=False, default=None)
    year = models.IntegerField()
    dual_degree = models.BooleanField(default=False)
    # choices in charfield #validators
    company = models.CharField(max_length=100, null=False, default=None)
    github_id = models.URLField(max_length=100, null=True, blank=True)
    linkedin_id = models.URLField(max_length=100, null=True, blank=True)
    image = models.URLField(
        default="http://uilove.in/realestate/listo/preview/img/profile-placeholder.jpg"
    )

    def __str__(self):
        return self.name
