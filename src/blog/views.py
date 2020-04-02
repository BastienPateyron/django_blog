from django.shortcuts import render

# Un post est une liste de dictionnaires
posts = [
   {
      'author': 'Bastien',
      'title': 'Blog Post 1',
      'content': 'First post content',
      'date_posted': '1 Avril 2020'
   },
     {
      'author': 'Jane Doe',
      'title': 'Blog Post 2',
      'content': 'Second post content',
      'date_posted': '2 Avril 2020'
   }
]

# Une fonction correspond à une vue
def home(request):
   context = {
      'posts': posts
   }
   return render(request, 'blog/home.html', context)


def about(request):
   return render(request, 'blog/about.html', {'title': 'About'})
