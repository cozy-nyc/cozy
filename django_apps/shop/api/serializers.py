from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    StringRelatedField
    )
from django_apps.shop.models import Category, SubCategory, Item, Listing, Transaction


#------------------------------------------------------------------------------
#Category
#------------------------------------------------------------------------------

class CategoryListSerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = [
            'id',
            'name',
        ]

class CategoryDetailSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name'
            'slug'
        ]

#------------------------------------------------------------------------------
#subCategory
#------------------------------------------------------------------------------


class SubCategoryCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = SubCategory
        fields = [
            'name',
            'parent',
        ]


class SubCategoryDetailSerializer(ModelSerializer):

    class Meta:
        model = SubCategory
        fields = [
            'id',
            'name',
            'parent',
        ]

class SubCategoryListSerializer(ModelSerializer):

    class Meta:
        model = SubCategory
        fields = [
            'id',
            'name',
            'parent',
        ]


#------------------------------------------------------------------------------
#Items
#------------------------------------------------------------------------------



class ItemCreateUpdateSerializer(ModelSerializer):

    class Meta:
        model = Item
        fields = [
            'name',
            'description',
            'material',
            'category',
            'subCatergory'
        ]

class ItemDetailSeralizer(ModelSerializer):
    class Meta:
        listings = StringRelatedField(many = True)
        category = CategoryDetailSerializer(read_only = True)
        subCatergory = SubCategoryDetailSerializer(read_only = True)
        model = Item
        fields = [
            'name',
            'description',
            'material',
            'category',
            'subCategory',
            'avgSoldPrice',
            'lowestCurrListing',
            'highestCurrListing',
            'lowestSoldListing',
            'highestSoldListing',
            'lastActive',
            'visible',
            'stock',
            'listings'
        ]

class ItemListlSeralizer(ModelSerializer):
    class Meta:
        category = CategoryDetailSerializer(read_only = True)
        subCatergory = SubCategoryDetailSerializer(read_only = True)
        model = Item
        fields = [
            'name',
            'description',
            'material',
            'category',
            'subCategory',
            'lastActive',
            'visible',
            'stock',
        ]
#------------------------------------------------------------------------------
#Listing
#------------------------------------------------------------------------------


class ListingCreateUpdateSerializer(ModelSerializer):

    class Meta:
        model = Listing
        fields = [
            'item',
            'conditionRating',
            'location',
            'price',
            'size',
        ]

class ListingDetailSeralizer(ModelSerializer):

    class Meta:
        model = Listing
        item = ItemDetailSeralizer(read_only = True)
        fields = [
            'seller',
            'item',
            'conditionRating',
            'description',
            'location',
            'price',
            'size',
            'available',
            'created',
        ]

class ListingListSeralizer(ModelSerializer):

    class Meta:
        item = ItemDetailSeralizer(read_only = True)
        model = Listing
        fields = [
            'item',
            'conditionRating',
            'price',
            'size',
            'available',
            'created',
        ]


#------------------------------------------------------------------------------
#Transaction
#------------------------------------------------------------------------------

class TransactionCreateUpdateSerializer(ModelSerializer):

    class Meta:
        model = Transaction
        fields = [
            'seller',
            'buyer',
            'amountExchanged',
            'deliveryAddress',
            'receiveAddress',
            'listing'
        ]



class TransactionSerializer(ModelSerializer):

    class Meta:
        model = Transaction
        fields = '__all__'
