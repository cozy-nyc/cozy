from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from profiles.models import Profile

class SignUpForm(UserCreationForm):
    displayName = forms.CharField(max_length=20, help_text='Required.')

    class Meta:
        model = User
        fields = ('displayName','email', 'first_name', 'last_name', 'password1', 'password2', )

# Placements for user update
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ()

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ()
