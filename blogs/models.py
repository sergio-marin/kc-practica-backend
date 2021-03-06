from django.core.urlresolvers import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models


class Blog(models.Model):
    blogger = models.OneToOneField(User, related_name="blog")
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=350, null=True, blank=True, default="")
    creation_date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        """
        Devuelve la url de un blog
        :return: string
        """
        return reverse('blog_detail', args=[self.blogger.username])

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, primary_key=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Post(models.Model):
    blog = models.ForeignKey(Blog, related_name="posts")
    title = models.CharField(max_length=200)
    introduction = models.TextField(max_length=350)
    body = models.TextField()
    media_url = models.URLField(blank=True, null=True)
    categories = models.ManyToManyField(Category, related_name="posts")
    published_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
