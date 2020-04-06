from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfilUpdateForm

def register(request):
   if request.method == 'POST':
      form = UserRegisterForm(request.POST)
      if form.is_valid():
         form.save() # Enregistre l'utilisateur en base
         username = form.cleaned_data.get('username')
         messages.success(request, f'Your account has been created! You are now able to login ! {username} !') # Chaine formatée
         return redirect('blog-home')
   else:
      form = UserRegisterForm()
   return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
   if request.method == 'POST':
      
      # Sauvegarde de la nouvelle image
      u_form = UserUpdateForm(request.POST, instance=request.user)
      p_form = ProfilUpdateForm(request.POST,      # On passe les données du form
                                request.FILES,     # On passe la photo du form
                                instance=request.user.profile)
                                
      if u_form.is_valid() and p_form.is_valid():
         
         # Sauvegarde des données
         u_form.save()
         p_form.save()
      
         messages.success(request, f'Your account has been updated !') # Chaine formatée
         return redirect('profile') # Pour éviter la popup qui demande le renvoi des infos

   else:
      u_form = UserUpdateForm(instance=request.user)
      p_form = ProfilUpdateForm(instance=request.user.profile)

   context = {
      'u_form': u_form,
      'p_form': p_form
   }
   return render(request, 'users/profile.html', context)
