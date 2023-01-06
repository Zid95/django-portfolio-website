from django.db import models


class Self(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='profile/', null=True, blank=True)
    twitter = models.URLField(max_length=100, null=True, blank=True)
    facebook = models.URLField(max_length=100, null=True, blank=True)
    instagram = models.URLField(max_length=100, null=True, blank=True)
    skype = models.URLField(max_length=100, null=True, blank=True)
    linkedin = models.URLField(max_length=100, null=True, blank=True)
    position1 = models.TextField(
        max_length=100, null=True, blank=True)
    position2 = models.TextField(
        max_length=100, null=True, blank=True)
    position3 = models.TextField(
        max_length=100, null=True, blank=True)
    position4 = models.TextField(
        max_length=100, null=True, blank=True)

    def __str__(self) -> str:
        return self.name
