from django.contrib import admin
from .models import Post

# Enregistrer les modèles ici pour les consulter dans le dashboard admin
admin.site.register(Post)