from django import forms
from django.forms import ModelForm
from .models import listing

class PostListingForm(ModelForm):

    class Meta:
        model = listing

        fields=['item_name', 'price', 'conditionRating', 'size', 'description', 'location']
