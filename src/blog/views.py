from django.shortcuts import render
from django.views.generic import (
   ListView, 
   DetailView, 
   CreateView
)
from .models import Post
from django.contrib import messages

# On met ".models" car le fichier est dans le même répertoire que la vue

# Une fonction correspond à une vue
def home(request):
   context = {
      'posts': Post.objects.all()
   }
   return render(request, 'blog/home.html', context)


class PostListView(ListView):
   model = Post
   template_name = 'blog/home.html'
   context_object_name = 'posts'    # Les objets seront contenus dans la variable 'posts'

   ordering = ['-date_posted']


class PostDetailView(DetailView):
   model = Post
   

class PostCreateView(CreateView):
   model = Post
   fields = ['title', 'content']

   def form_valid(self, form):
      form.instance.author = self.request.user # On définit l'auteur avant validation
      messages.success(self.request, f'Post Created !')
      return super().form_valid(form)


def about(request):
   return render(request, 'blog/about.html', {'title': 'About'})










# Un post est une liste de dictionnaires
# posts = [
#    {
#       'author': 'Bastien',
#       'title': 'Blog Post 1',
#       'content': 'First post content',
#       'date_posted': '1 Avril 2020'
#    },
#      {
#       'author': 'Jane Doe',
#       'title': 'Blog Post 2',
#       'content': 'Second post content',
#       'date_posted': '2 Avril 2020'
#    }
# ]
