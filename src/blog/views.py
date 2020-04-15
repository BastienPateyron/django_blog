from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
   ListView, 
   DetailView, 
   CreateView,
   UpdateView,
   DeleteView
)
from .models import Post
from django.contrib import messages
from django.urls import reverse_lazy

# On met ".models" car le fichier est dans le même répertoire que la vue

### Function-Based Views ###

# Une fonction correspond à une vue
def home(request):
   context = {
      'posts': Post.objects.all()
   }
   return render(request, 'blog/home.html', context)             


def about(request):
   return render(request, 'blog/about.html', {'title': 'About'})



### Class-Based Views ###

class PostListView(ListView):
   model = Post
   template_name = 'blog/home.html'
   context_object_name = 'posts'    # Les objets seront contenus dans la variable 'posts'

   ordering = ['-date_posted']

   paginate_by = 5                  # Pagine avec 5 post par page


class UserPostListView(ListView):
   model = Post
   template_name = 'blog/user_posts.html'
   context_object_name = 'posts'    # Les objets seront contenus dans la variable 'posts'
   ordering = ['-date_posted']
   paginate_by = 5                  # Pagine avec 5 post par page

   def get_queryset(self):
      user = get_object_or_404(User, username=self.kwargs.get('username'))
      return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
   model = Post
   
# Une classe MixIn doit TOUJOURS être passée en PREMIER dans les arguments
class PostCreateView(LoginRequiredMixin, CreateView):
   model = Post
   fields = ['title', 'content']

   def form_valid(self, form):
      form.instance.author = self.request.user # On définit l'auteur avant validation
      messages.success(self.request, f'Post Created !')
      return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,
                     UserPassesTestMixin,
                     UpdateView):
   model = Post
   fields = ['title', 'content']

   def test_func(self):
      post = self.get_object()                  # Récupération du post
      return (self.request.user == post.author) # On vérifie qu'on est l'auteur du post

   def form_valid(self, form):
      form.instance.author = self.request.user
      messages.success(self.request, f'Post Updated !')
      return super().form_valid(form)


class PostDeleteView(LoginRequiredMixin,
                     UserPassesTestMixin,
                     DeleteView):
   model = Post
   success_url = reverse_lazy('blog-home') # Renvoie juste '/' mais en DRY

   def test_func(self):
      post = self.get_object()                 
      return (self.request.user == post.author)
      











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
