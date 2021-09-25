from django.db import models


class TeamModel(models.Model):
    name = models.CharField(max_length=50, null=False)
    post = models.CharField(max_length=50, null=False)
    created_at = models.DateTimeField(auto_now_add=True)


# Create your models here.
