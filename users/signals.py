# these are used for creating imediate upload when there is image 

from django.db.models.signals import post_save
from django.contrib.auth.moldels import User 
from django.dispatch import receiver
from models import Profile

# To create profile picture

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.object.create(user=instance)

# To save pfofile 
@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    if created:
        instance.profile.save()

