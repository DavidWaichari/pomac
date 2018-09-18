from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class CustomUser(AbstractUser):
    # Add additional fields here. For example, a global-friendly name field
    AbstractUser._meta.get_field('email')._unique = True
    AbstractUser._meta.get_field('username')._unique = False
    residence = models.CharField(max_length=50, blank=True)
    profession = models.CharField(max_length=50, blank=True)
    contact = models.CharField(max_length=15, blank=True)
    def __str__(self):
        if(self.first_name == '' and self.last_name ==''):
            return self.email
        return self.first_name+ ' '+ self.last_name