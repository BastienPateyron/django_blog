from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
   email = forms.EmailField()

   # Les champs avec lesquels on compte intéragir
   # Par exemple, le champ 'email' ne fonctionne pas si on ne fait pas ça
   class Meta:
      model = User
      fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
   email = forms.EmailField()

   class Meta:
      model = User
      fields = ['username', 'email']


class ProfilUpdateForm(forms.ModelForm):
   class Meta:
      model = Profile
      fields = ['image']

