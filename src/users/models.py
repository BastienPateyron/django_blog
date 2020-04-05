from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# PIL = Pillow

class Profile(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   image = models.ImageField(default='default.jpg', upload_to='profile_pics')
   # default: image par défaut de tous les utilisateurs
   # upload_to: répertoire ou sont stockées les photos uploadées

   def __str__(self):
      return f'{self.user.username} Profile'

   # Redéfinition de la méthode save de l'objet Profile
   def save(self):
      super().save()       # Appel de la méthode mère

      img = Image.open(self.image.path)

      # Check si l'img est supérieure à 300px
      if img.height > 300 or img.width > 300:
         output_size = (300, 300)
         img.thumbnail(output_size)    # Redimentionnement
         img.save(self.image.path)     # Ecrase l'ancienne img


      # TODO Supprimer l'ancienne photo