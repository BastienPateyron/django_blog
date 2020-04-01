from django.shortcuts import render
from django.http import HttpResponse

# Une fonction correspond à une vue
def home(request):
   return HttpResponse('<h1>Blog Home</h1>')
