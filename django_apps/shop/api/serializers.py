from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    StringRelatedField,
    RelatedField,
    ReadOnlyField
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
            'subCategory',
            'available',
            'image '
        ]

class ItemDetailSeralizer(ModelSerializer):
    class Meta:
        listings = StringRelatedField(many = True)
        category = CategoryDetailSerializer(read_only = True)
        subCatergory = SubCategoryDetailSerializer(read_only = True)
        image = SerializerMethodField()
        model = Item
        fields = [
            'id',
            'slug',
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

        def get_image(self,obj):
            try:
                image = obj.image.url
            except:
                image = None
            return image

class ItemListlSeralizer(ModelSerializer):
    class Meta:
        category = CategoryDetailSerializer(read_only = True)
        subCatergory = SubCategoryDetailSerializer(read_only = True)
        image = SerializerMethodField()

        model = Item
        fields = [
            'id',
            'slug',
            'name',
            'category',
            'subCategory',
            'lastActive',
            'visible',
            'stock',
            'avgSoldPrice',
            'lowestCurrListing',
            'highestCurrListing',
        ]
        def get_image(self,obj):
            try:
                image = obj.image.url
            except:
                image = None
            return image
#------------------------------------------------------------------------------
#Listing
#------------------------------------------------------------------------------


class ListingCreateUpdateSerializer(ModelSerializer):


    class Meta:
        model = Listing
        fields = [
            'item',
            'image',
            'conditionRating',
            'location',
            'price',
            'size',
            'image'
        ]

class ListingDetailSeralizer(ModelSerializer):

    item_name = ReadOnlyField
    item_slug = ReadOnlyField
    image = SerializerMethodField()


    class Meta:
        model = Listing
        fields = [
            'id',
            'seller',
            'image',
            'item',
            'item_name',
            'item_slug',
            'conditionRating',
            'description',
            'location',
            'price',
            'size',
            'available',
            'created',
        ]
    def get_image(self,obj):
        try:
            image = obj.image.url
        except:
            image = None
        return image

class ListingListSeralizer(ModelSerializer):

    item_name = ReadOnlyField
    item_slug = ReadOnlyField
    image = SerializerMethodField()

    class Meta:
        model = Listing
        fields = [
            'id',
            'item',
            'image',
            'item_name',
            'item_slug',
            'conditionRating',
            'price',
            'size',
            'available',
            'created',

        ]
    def get_image(self,obj):
        try:
            image = obj.image.url
        except:
            image = None
        return image

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
            'listing',
            'ratingSeller',
            'ratingBuyer',
            'isValid'

        ]

class TransactionDetailSerializer(ModelSerializer):
    class Meta:
        model = Transaction

        fields = '__all__'

class TransactionListSerializer(ModelSerializer):
    class Meta:

        model = Transaction

        fields = '__all__'


class TransactionSerializer(ModelSerializer):

    class Meta:
        model = Transaction
        fields = '__all__'
