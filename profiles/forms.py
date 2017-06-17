from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from profiles.models import Profile

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'email', 'password1', 'password2', )

# Placements for user update
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ()

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ()
