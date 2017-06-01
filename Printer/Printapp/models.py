from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    money = models.IntegerField(default=0)

class Model_project(models.Model):
    model_name = models.CharField(max_length=20)
    model_owner = models.CharField(max_length=20)
    model_price = models.IntegerField(default=20)
    model_introd = models.TextField()
    model_image = models.ImageField(upload_to='model/model_image',default='model/model_image')
    model_file = models.FileField(upload_to='model/model_file',default='model/model_file')
    model_date = models.DateTimeField(default = timezone.now)

class StlFile(models.Model):
    stl_file = models.FileField(upload_to='stl_file',default='stl_file')
    stl_owner = models.CharField(max_length=20)
    stl_name = models.CharField(max_length=20)
    stl_image = models.ImageField(upload_to='stl_file/stl_image',default='stl_file/stl_image')
    stl_date = models.DateTimeField(default = timezone.now)

class Printer(models.Model):
    #id = models.UUIDField(primary_key=True, default=uuid.uuid, editable=False)
    Printer_name = models.CharField(max_length=20,default='name')
    max_x = models.IntegerField()
    max_y = models.IntegerField()
    max_z = models.IntegerField()
    nozzle_nr = models.IntegerField(default =1)
    layer_height = models.DecimalField( default = 0.2,max_digits=3,decimal_places=2)
    shell_thick = models.DecimalField( default = 0.8,max_digits=3,decimal_places=2)
    Infill = models.IntegerField(default=20)
    Print_Speed = models.IntegerField(default = 60)
    nozzle_temperature = models.IntegerField(default=220)
    bed_temperature = models.IntegerField(default=60)
    Support_Angle = models.IntegerField(default = 60) 
    Retract_Length = models.DecimalField(default = 5,max_digits=3,decimal_places=2)
    Retract_Speed = models.DecimalField(default = 25,max_digits=4,decimal_places=2)
    support_range = models.CharField(max_length=20,default='everywhere')
    Plate_Type = models.CharField(max_length=20,default='Brim')
    pr_type = models.CharField(max_length=20)
    filament = models.CharField(max_length=20,default='PLA')
    owner = models.CharField(max_length=20) #unwritten
    pr_state = models.IntegerField(default = 0)
    pr_date = models.DateTimeField(default = timezone.now)


def create_user_profile(sender, instance,created, **kwargs):
    if created:
        profile = UserProfile()
        profile.user = instance
        profile.save()




User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
post_save.connect(create_user_profile, sender=User)