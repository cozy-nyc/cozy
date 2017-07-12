from django import forms
from django.forms import ModelForm
from .models import Listing, Item

class PostListingForm(ModelForm):
    item_name = forms.CharField(max_length=200)
    item_category = forms.CharField(max_length=16)
    item_subCategory = forms.CharField(max_length=16)
    # item_brand


    class Meta:
        model = Listing

        fields=['item_name', 'item_category', 'item_subCategory', 'size', 'conditionRating', 'description','price', 'location']

    def FindItem(self):
        # If user pick a other as suggestion then CreateItem() with item name
        # Else
            # If there's a item similar to the item_name given then suggest that item(s)
            # Else CreateItem()
        return

    def CreateItem(self):
        return
