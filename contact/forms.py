from django import forms

class contactForm(forms.Form):
    """
    The form used to submit an email to the contacts

    name: string that contains the name of the user
    email: the string that contains the email for
    message: the string that contains the message that is to be delievered to the cozy admins
    """
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
