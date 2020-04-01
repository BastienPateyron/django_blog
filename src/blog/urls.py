from django.urls import path
from . import views
# Le ' . ' fait référence au répertoire courant de ce fichier, donc de blog/

# Un path vide comme suit: '' pointe vers la racine du site
urlpatterns = [
   path('', views.home, name = 'blog-home'),
   path('about/', views.about, name = 'blog-about'),
]