from django.db.models.signals import pre_save, post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# Fonction qu'on veut lancer à chaque création d'utilisateur
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
   if created:
      Profile.objects.create(user=instance)

# Sauvegarde le profil en cas de modification
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
   instance.profile.save()