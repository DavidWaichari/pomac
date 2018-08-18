from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class CustomUser(AbstractUser):
    # Add additional fields here. For example, a global-friendly name field
    name = models.CharField(blank=True, max_length=255)
    AbstractUser._meta.get_field('email')._unique = False
    AbstractUser._meta.get_field('username')._unique = False

    def __str__(self):
        return self.email

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    residence = models.TextField(max_length=30, blank=True)
    profession = models.DateField(null=True, blank=True)
    email_confirmed = models.BooleanField(default=False)


@receiver(post_save, sender=CustomUser)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
