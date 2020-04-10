from django.urls import path
from .views import (
   PostListView, 
   PostDetailView,
   PostCreateView
)
from . import views
# Le ' . ' fait référence au répertoire courant de ce fichier, donc de blog/

# Un path vide comme suit: '' pointe vers la racine du site
urlpatterns = [
   path('', PostListView.as_view(), name = 'blog-home'),
   path('post/<int:pk>/', PostDetailView.as_view(), name = 'post-detail'),
   path('post/new/', PostCreateView.as_view(), name = 'post-create'),
   path('about/', views.about, name = 'blog-about'),
]