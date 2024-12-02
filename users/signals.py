from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Workers

@receiver(post_save, sender=User)
def create_worker_profile(sender, instance, created, **kwargs):
    if created:
        Workers.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_worker_profile(sender, instance, **kwargs):
    try:
        instance.worker_profile.save()
    except Workers.DoesNotExist:
        pass
