from django import forms

class contactForm(forms.Form):
    name = forms.CharField(
        required=True,
        max_length=40,
        min_length=1
        )
    email = forms.EmailField(
        required=True
        )
    message = forms.CharField(
        required=True,
        widget = forms.Textarea
        )
