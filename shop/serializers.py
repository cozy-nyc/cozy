
from rest_framework import serializers
from .models import Category, SubCategory, Item, Listing, Transaction

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

class SubCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = SubCategory
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = '__all__'

class ListingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Listing
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = '__all__'
