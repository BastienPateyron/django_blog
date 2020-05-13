from django.test import SimpleTestCase
from django.urls import reverse, resolve
from users.views import (
   register,
   profile,
   UserLoginView,
)
from django.contrib.auth import views as auth_views
from mixer.backend.django import mixer
from django.urls.exceptions import NoReverseMatch
import pytest

@pytest.mark.parametrize('url, expected', [
   ('register', register),
   ('profile', profile),
])
def test_url_list_functionbased_resolve(url, expected):
   assert resolve(reverse(url)).func == expected
   

@pytest.mark.parametrize('url, expected', [
   ('login', UserLoginView),
   ('logout', auth_views.LogoutView),
   ('password_reset', auth_views.PasswordResetView),
   ('password_reset_done', auth_views.PasswordResetDoneView),
   ('password_reset_complete', auth_views.PasswordResetCompleteView),
])
def test_url_list_classbased_resolve(url, expected):
   assert resolve(reverse(url)).func.view_class == expected

def test_url_password_confirm():
   with pytest.raises(NoReverseMatch) as exception:
      resolve(reverse('password_reset_confirm'))
      assert 'with no arguments found' in str(exception.value), "Should return an exception because the route don't exist"

   with pytest.raises(NoReverseMatch) as exception:
      resolve(reverse('password_reset_confirm', args=['test_udb64']))
      assert 'with arguments' in str(exception.value), "Exception because one argument is missing"
      assert 'not found' in str(exception.value), "Exception because one argument is missing"
  
   assert resolve(reverse('password_reset_confirm', args=['test_uidb64', 'test_token'])).func.view_class == auth_views.PasswordResetConfirmView


# TODO
# def test_url_add_resolve():
#    url = reverse('add')
#    assert resolve(url).func.view_class == ProjectCreateView

# def test_url_detail_resolve():
#    url = reverse('detail', args=['some_slug'])
#    assert resolve(url).func == project_detail
