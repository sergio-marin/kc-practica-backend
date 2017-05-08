from django.contrib.auth.models import User
from django.db import models


class Blog(models.Model):
    blogger = models.OneToOneField(User, related_name="blog")
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=350, null=True, blank=True, default="")
    creation_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name
