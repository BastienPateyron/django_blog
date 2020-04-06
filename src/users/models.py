from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# PIL = Pillow

class Profile(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   image = models.ImageField(default='default.jpg', upload_to='profile_pics')
   # default: image par défaut de tous les utilisateurs
   # upload_to: répertoire ou sont stockées les photos uploadées

   __original_image = None

   def __str__(self):
      return f'{self.user.username} Profile'

   # Supprimer l'ancienne photo
   def __init__(self, *args, **kwargs):
      super(Profile, self).__init__(*args, **kwargs)
      self.__original_image = self.image


   # Redéfinition de la méthode save de l'objet Profile
   def save(self):

      # Si on change d'image, suppression de l'ancienne
      if self.image != self.__original_image:
         img = self.__original_image
         if img.name != 'default.jpg': # Epargne l'img par défaut
            img.storage.delete(img.name)
            print(f'Image {img.url} supprimée')
         
      # Sauvegarde
      super().save()                   

      # Vérification dimensions
      img = Image.open(self.image.path)

      if img.height > 300 or img.width > 300:
         output_size = (300, 300)
         img.thumbnail(output_size)    # Redimentionnement
         img.save(self.image.path)     # Ecrase l'ancienne img


