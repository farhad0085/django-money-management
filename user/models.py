from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from common.currencies import CURRENCIES


class UserProfile(models.Model):
    """User profile for extending default django User model"""

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile")
    full_name = models.CharField(max_length=60, blank=True, null=True)
    phone_number = models.CharField(null=True, max_length=15)
    profile_picture = models.ImageField(upload_to="%Y/%B/%d/images/dp")
    currency = models.CharField(max_length=20, choices=CURRENCIES, default='USD', blank=True)

    def __str__(self):
        return self.user.username

# signals
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """create profile for user."""

    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.user_profile.save()