from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django import forms


'''class Register(models.Model):
    username=models.CharField(max_length=250)
    first=models.CharField(max_length=250)
    last=models.CharField(max_length=240)
    password=models.CharField(max_length=200)'''

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll = models.IntegerField(null=True, blank=True)
    phone = models.IntegerField(null=True,blank=True)
    address = models.CharField(null=True, max_length=50, blank=True)
    pin = models.IntegerField(null=True, blank=True)
    city = models.CharField(null=True, max_length=50, blank=True)
    parent_name = models.CharField(null=True, max_length=50, blank=True)
    parent_phone = models.IntegerField(null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)


# Create your tests here.

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

User.profile = property(lambda u: Profile.objects.get_or_create(user=u)[0])

