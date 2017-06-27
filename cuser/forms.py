from django import forms
from django.contrib.auth.forms import UserCreationForm
from cuser.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    displayName = forms.CharField(max_length=40, help_text='Required.')

    class Meta:
        model = User
        fields = ('email', 'displayName', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        displayName = self.cleaned_data.get('displayName')
        if email and User.objects.filter(displayName=displayName).exclude(email=email).exists():
            raise forms.ValidationError(u'Display Name must be unique.')
        return email
