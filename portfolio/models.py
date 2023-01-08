from django.db import models


class Self(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='profile/', default='profile/0.png')
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
    image = models.ImageField(upload_to='about/', default='about/0.png')
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
    main_desc = models.TextField(max_length=450, null=True, blank=True)
    total1 = models.IntegerField(null=True, blank=True)
    title1 = models.CharField(max_length=50, null=True, blank=True)
    desc1 = models.CharField(max_length=50, null=True, blank=True) 
    total2 = models.IntegerField(null=True, blank=True)
    title2 = models.CharField(max_length=50, null=True, blank=True)
    desc2 = models.CharField(max_length=50, null=True, blank=True) 
    total3 = models.IntegerField(null=True, blank=True)
    title3 = models.CharField(max_length=50, null=True, blank=True)
    desc3 = models.CharField(max_length=50, null=True, blank=True) 
    total4 = models.IntegerField(null=True, blank=True)
    title4 = models.CharField(max_length=50, null=True, blank=True)
    desc4 = models.CharField(max_length=50, null=True, blank=True) 

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


class Resume(models.Model):
    #  desc for section Resume
    desc = models.TextField(max_length=450, null=True, blank=True)
    # end desc for section Resume
    # cv section 1
    main_title = models.CharField(max_length=50, null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    subtitle = models.CharField(max_length=150, null=True, blank=True)
    adress = models.CharField(max_length=25,null=True, blank=True)
    phone = models.CharField(max_length=30, null=True, blank=True)
    Email = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self) -> str:
        return "Resume Section"


# cv section 2
class Resume1(models.Model):
    main_title = models.CharField(max_length=50, null=True, blank=True)
    title = models.CharField(max_length=50, null=True, blank=True)
    period = models.CharField(max_length=20, null=True, blank=True)
    place = models.CharField(max_length=50, null=True, blank=True)
    desc = models.TextField(max_length=450, null=True, blank=True)

    def __str__(self) -> str:
        return "Resume1 Section"

# cv section 3
class Resume2(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    period = models.CharField(max_length=20, null=True, blank=True)
    place = models.CharField(max_length=50, null=True, blank=True)
    desc = models.TextField(max_length=450, null=True, blank=True)

    def __str__(self) -> str:
        return "Resume2 Section"

# cv section 4
class Resume3(models.Model):
    main_title = models.CharField(max_length=50, null=True, blank=True)
    title = models.CharField(max_length=50, null=True, blank=True)
    period = models.CharField(max_length=20, null=True, blank=True)
    place = models.CharField(max_length=50, null=True, blank=True)
    desc1 = models.TextField(max_length=450, null=True, blank=True)
    desc2 = models.TextField(max_length=450, null=True, blank=True)
    desc3 = models.TextField(max_length=450, null=True, blank=True)
    desc4 = models.TextField(max_length=450, null=True, blank=True)

    def __str__(self) -> str:
        return "Resume3 Section"


# cv section 5
class Resume4(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    period = models.CharField(max_length=20, null=True, blank=True)
    place = models.CharField(max_length=50, null=True, blank=True)
    desc1 = models.TextField(max_length=450, null=True, blank=True)
    desc2 = models.TextField(max_length=450, null=True, blank=True)
    desc3 = models.TextField(max_length=450, null=True, blank=True)
    desc4 = models.TextField(max_length=450, null=True, blank=True)

    def __str__(self) -> str:
        return "Resume4 Section"


class Services(models.Model):
    main_desc = models.TextField(max_length=450, null=True, blank=True)
    title1 = models.CharField(max_length=50, null=True, blank=True)
    desc1 = models.TextField(max_length=300, null=True, blank=True)
    title2 = models.CharField(max_length=50, null=True, blank=True)
    desc2 = models.TextField(max_length=300, null=True, blank=True)
    title3 = models.CharField(max_length=50, null=True, blank=True)
    desc3 = models.TextField(max_length=300, null=True, blank=True)
    title4 = models.CharField(max_length=50, null=True, blank=True)
    desc4 = models.TextField(max_length=300, null=True, blank=True)
    title5 = models.CharField(max_length=50, null=True, blank=True)
    desc5 = models.TextField(max_length=300, null=True, blank=True)
    title6 = models.CharField(max_length=50, null=True, blank=True)
    desc6 = models.TextField(max_length=300, null=True, blank=True)

    def __str__(self) -> str:
        return "Services Section"
