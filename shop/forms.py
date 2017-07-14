from django import forms
from django.forms import ModelForm
from .models import Listing, Item

class PostListingForm(ModelForm):
    """This is a form for users to create listings
    """
    item_name = forms.CharField(max_length=200)
    item_category = forms.CharField(max_length=16)
    item_subCategory = forms.CharField(max_length=16)
    # item_brand


    class Meta:
        model = Listing

        fields=['item_name', 'item_category', 'item_subCategory', 'size', 'conditionRating', 'description','price', 'location']

    def FindItem(self):
        """This function checks if a item exist

        If the 'item_name' matches or is similar to an existing 'item' in the database
        than that item will be suggested and auto fill the rest of item info.
        Else calls 'CreateItem()'
        """
        # If user pick a other as suggestion then CreateItem() with item name
        # Else
            # If there's a item similar to the item_name given then suggest that item(s)
            # Else CreateItem()
        return

    def CreateItem(self):
        """This function creates an item

        Note:
            Might move this function
        """
        return
