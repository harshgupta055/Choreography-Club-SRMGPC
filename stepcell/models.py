from django.db import models
from django.core.validators import FileExtensionValidator
from django.db.models.aggregates import Max
from django.db.models.base import Model
from django.db.models.fields import CharField
# Create your models here.

class CarouselItem(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to="CarouselItem/")

    def __str__(self):
        return str(self.id)

class YoutubeUpdate(models.Model):
    id = models.AutoField(primary_key=True)
    embed_link = models.CharField(max_length=1000,null=True,help_text='embed link from youtube, only src url will be taken')
    title = models.CharField(max_length=300,null=True,help_text='title')
    video_link = models.CharField(max_length=200,null=True,help_text='youtube video link')
    date = models.DateField()

    def __str__(self):
        return self.title

class OngoingEvent(models.Model):
    id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=200,null=True)
    event_poster = models.ImageField(upload_to="ongoingEvent/")
    event_registeration_date = models.DateField()
    event_link = models.CharField(help_text="registration page link for the event",max_length=300,null=True)

    def __str__(self):
        return self.event_name

class OngoingEventCarousel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,null=True,help_text="name of the event")
    class_name = models.CharField(max_length=50,default="not active",help_text="active class or not")
    image = models.FileField(upload_to="ongoingEventCarousel/",validators=[FileExtensionValidator(['jpg','png','jpeg'])])

    def __str__(self):
        return self.name

class OngoingEventRegisteration(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,blank=True)
    email = models.EmailField(max_length=300,blank=True)
    phone = models.IntegerField(blank=True)
    college = models.CharField(max_length=300,blank=True)
    field1 = models.CharField(max_length=200,blank=True)
    field2 = models.CharField(max_length=200,blank=True)
    field3 = models.CharField(max_length=200,blank=True)

    def __str__(self):
        return self.name

class Coordinator(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,blank=False,help_text='student name')
    branch = models.CharField(max_length=300,help_text='branch')
    phone = models.CharField(help_text="10-digits number",blank=True,max_length=12)
    linkedin_link = models.CharField(max_length=300,default="#",help_text='linkedin profile link')
    insta_link = models.CharField(max_length=300,default="#",help_text='instagram profile link')
    profile_image = models.FileField(upload_to="coordinators/",validators=[FileExtensionValidator(['jpg','png','jpeg'])])

    def __str__(self):
        return self.name

class VeteranCoordinator(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,blank=False,help_text='student name')
    branch = models.CharField(max_length=300,help_text='branch')
    phone = models.CharField(help_text="10-digits number",blank=True,max_length=12)
    linkedin_link = models.CharField(max_length=300,default="#",help_text='linkedin profile link')
    insta_link = models.CharField(max_length=300,default="#",help_text='instagram profile link')
    profile_image = models.FileField(upload_to="veteranCoordinators/",validators=[FileExtensionValidator(['jpg','png','jpeg'])])

    def __str__(self):
        return self.name

class AbhivyaktiEvent(models.Model):
    id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=200,null=True)
    event_desc = models.CharField(max_length=400,null=True,help_text="about event")
    event_poster = models.ImageField(upload_to="abhivyaktiEvent/",help_text="your image should be in size ratio 3:2")
    event_link = models.CharField(help_text="registration page link for the event",default="#",max_length=300,null=True)

    def __str__(self):
        return self.event_name

class AbhivyaktiPerformingEvent(models.Model):
    id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=200,null=True)
    event_desc = models.CharField(max_length=1000,null=True,help_text="about event")
    event_poster = models.ImageField(upload_to="abhivyaktiEvent/",help_text="your image should be in size ratio 3:2")

    def __str__(self):
        return self.event_name


class Team(models.Model):
    id = models.AutoField(primary_key=True)
    year = models.CharField(max_length=50,default='',help_text='batch year, starting year to end year. It must be 4 years. e.g. 2018-2022')
    student_name = models.CharField(max_length=100,null=False,help_text='student name')
    branch = models.CharField(max_length=200,help_text='branch')
    phone=models.CharField(help_text='10 digits phone number',max_length=12,blank=True)
    fb_link=models.CharField(max_length=300,help_text='facebook profile link',default="#",blank=True)
    linkedin_link=models.CharField(max_length=300,help_text='linkedin profile link',default="#",blank=True)
    insta_link=models.CharField(max_length=300,help_text='instagram profile link',default="#",blank=True)
    yt_link=models.CharField(max_length=300,help_text='youtube channel link',default="#",blank=True)
    image=models.FileField(validators=[FileExtensionValidator(['jpg','png','jpeg'])],upload_to="team/")

    def __str__(self):
        return self.student_name

class ControlVolunteer(models.Model):
    id = models.AutoField(primary_key=True)
    year = models.CharField(max_length=50,help_text='Volunteer year which we want to display')
    
    def __str__(self):
        return self.year

class ControlVeteran(models.Model):
    id = models.AutoField(primary_key=True)
    year = models.CharField(max_length=50,help_text='Volunteer year which we want to display')
    
    def __str__(self):
        return self.year

class Gallery(models.Model):
    id = models.AutoField(primary_key=True)
    event = models.CharField(max_length=300,help_text='event')
    image = models.FileField(validators=[FileExtensionValidator(['jpg','png'])],upload_to="gallery/",help_text="Image dimension must be in 3:2 ratio")

    def __str__(self):
        return self.event