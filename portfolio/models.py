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


class About(models.Model):
    freelance = [
        ('Available', 'Available'),
        ('Not Available', 'Not Available')
    ]
    introduction = models.TextField(max_length=450, null=True, blank=True)
    title = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(upload_to='about/', null=True, blank=True)
    subtitle = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    Website = models.URLField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=30, null=True, blank=True)
    City = models.CharField(max_length=50, null=True, blank=True)
    Age = models.IntegerField(null=True, blank=True)
    Degree = models.CharField(max_length=30, null=True, blank=True)
    Email = models.CharField(max_length=30, null=True, blank=True)
    status = models.CharField(
        max_length=20, choices=freelance, null=True, blank=True)
    desc = models.TextField(max_length=350, null=True, blank=True)

    def __str__(self) -> str:
        return "About Section"


class Facts(models.Model):
    desc = models.TextField(max_length=450, null=True, blank=True)
    happyclients = models.IntegerField(null=True, blank=True)
    Projects = models.IntegerField(null=True, blank=True)
    Support = models.IntegerField(null=True, blank=True)
    Hardworks = models.IntegerField(null=True, blank=True)

    def __str__(self) -> str:
        return "Facts Section"

class Skills(models.Model):
    desc = models.TextField(max_length=450, null=True, blank=True)
    skill1_t = models.CharField(max_length=25,null=True, blank=True)
    skill1_v = models.IntegerField(null=True, blank=True)
    skill2_t = models.CharField(max_length=25,null=True, blank=True)
    skill2_v = models.IntegerField(null=True, blank=True)
    skill3_t = models.CharField(max_length=25,null=True, blank=True)
    skill3_v = models.IntegerField(null=True, blank=True)
    skill4_t = models.CharField(max_length=25,null=True, blank=True)
    skill4_v = models.IntegerField(null=True, blank=True)
    skill5_t = models.CharField(max_length=25,null=True, blank=True)
    skill5_v = models.IntegerField(null=True, blank=True)
    skill6_t = models.CharField(max_length=25,null=True, blank=True)
    skill6_v = models.IntegerField(null=True, blank=True)

    def __str__(self) -> str:
        return "Skills Section"