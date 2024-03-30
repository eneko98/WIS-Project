from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import IndividualProfile, BandProfile

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, created, **kwargs):
    if created:
        # Here you might want to determine how to choose between IndividualProfile or BandProfile
        # For now, let's create an IndividualProfile as an example
        IndividualProfile.objects.create(user=instance)
