from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from .manager import CategoryManager, SubCatergoryManager, ItemManager, ListingManager, TransactionManager
from django.db.models.signals import post_save
import datetime


class Category(models.Model):
    """This is a model for a predetermined list of clothing categories.

    List:
        Jackets, shirts, sweaters, sweatshirts, pants, t-shirts, hats, accessories, skate, bike, and other

    Attributes:
        name: A string of the name of a category
        slug: A slug to make our links more presentable on the web app
    """
    name = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=50, db_index=True, unique=True)
    objects = CategoryManager()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('shop:item_list_by_category', args=[self.slug])


class SubCategory(models.Model):
    """
        This is a model for a list of clothing sub-categories that are either
        predetermind or user input.

        Attributes:
            name: A string of the name of a sub-category
            parent: foreign key to the Category. the class SubCategory is a
            child to category.
    """
    name = models.CharField(max_length=16)
    parent = models.ForeignKey(Category, related_name = 'subCats')
    objects = SubCatergoryManager()


    def __str__(self):
        return self.name


    class Meta:
        ordering = ('name',)
        verbose_name = 'subcategory'
        verbose_name_plural = 'subcategories'



# Needs to be moved to profile
# class Brand(models.Model):
#     name = models.CharField(max_length=32)
#     description = models.TextField(blank=True)
#     location = models.CharField(max_length = 50)
#     owner = models.ForeignKey('profiles.Profile')
#     email = models.EmailField(blank=True)
#
#     def _str_(self):
#         return self.name


class Item(models.Model):
    """
        This is a model for items sold on the exchange.

        Attributes:
            name: A string of the name of the item
            slug: A slug to make our links more readable
            description: A string which should describe the item for the users
            materla: A string which should identify the materials used to make the item
            category: A foregin key to category to make items more organized
            subCategory: A foregin key to subCatergory to make our items even more organized
            avgSoldPrice: A number which will go through all listings to achieve the avgSoldPrice
            lowestCurrListing: A number which will represent the lowest current avaible listing. A query will be used to find this
            highestCurrListing: A number which will represent the highest current available listing. A query will be used to find this
            lowestSoldListing: A number which will represent the lowest price a listing has been sold for this item.
            highestSoldListing: A number which will represent the highest price a listing has been sold for that item.
            lastActive: A date and time which represent when the last time the item has been edited
            available: A boolean which represents whether there are listings avialble or not
            stock: a integer that represents the amount of listings that are availble for the user to buy
    """
    name = models.CharField(max_length=200, db_index=True, unique = True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField()
    # brand = models.ForeignKey(Brand)
    description = models.TextField(blank=True)
    material = models.TextField(blank=True)
    # related_name may not be needed. Research!!!
    category = models.ForeignKey(Category, related_name='Item')
    subCategory = models.ForeignKey(SubCategory)
    avgSoldPrice = models.DecimalField(
            default=1.00,
            validators=[MinValueValidator(1.0)],
            decimal_places=2,
            max_digits=10
            )
    lowestCurrListing = models.DecimalField(
            default=1.00,
            validators=[MinValueValidator(1.0)],
            decimal_places=2,
            max_digits=10
            )
    highestCurrListing = models.DecimalField(
            default=1.00,
            validators=[MinValueValidator(1.0)],
            decimal_places=2,
            max_digits=10
            )
    lowestSoldListing = models.DecimalField(
            default=1.00,
            validators=[MinValueValidator(1.0)],
            decimal_places=2,
            max_digits=10
            )
    highestSoldListing = models.DecimalField(
            default=1.00,
            validators=[MinValueValidator(1.0)],
            decimal_places=2,
            max_digits=10
            )
    lastActive = models.DateTimeField(default = timezone.now)
    visible = models.BooleanField(default = True)
    stock = models.PositiveIntegerField(
            default = 0
    )
    objects = ItemManager()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-lastActive',)
        index_together = (('id','slug'),)
        verbose_name_plural = 'Items'

    def get_absolute_url(self):
        return reverse('shop:item_detail', args=[self.id, self.slug])

    def __unicode__(self):
        return ('%d: %s' (self.id, self.name))





class Listing(models.Model):
    """
        This is a model for listings on the exchange.

        Attributes:
            name: A string of the name of the item that the listing is tied to
            seller: A foriegn key to a user object that is selling the listing
            conditionRating: A float between 1 and 10 that will represent the condition of the listing
            description: A string that will further describe the item to perspective buyers
            location: The locaton of the seller
            price:A decimal field which will represent how much the user wishes to sell the item for
            size: Characters which will represents the size of the product I.E: XL, 13, M
            available: A boolean which represents whether the item is on sale or not
            created = The date and time field that the listing was created
            updated = the date and time field the listing was last updated
    """
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, related_name='listings')
    image = models.ImageField()
    conditionRating = models.FloatField(
        default=5.0,
        validators=[MaxValueValidator(10.0), MinValueValidator(1.0)]
        )
    description = models.TextField(blank=True)
    #Change to location model
    location = models.CharField(max_length = 50)
    price = models.DecimalField(
        default=1.00,
        validators=[MinValueValidator(1.0)],
        decimal_places=2,
        max_digits=10,
    )
    size = models.CharField(max_length = 5, blank = True, null = True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = ListingManager()

    def __str__(self):
        return self.item.name


    def save(self, **kwargs):
        """
            This function is an override of the save function so that the item object
            will be automiatcally updated everytime there is  achange within the listing

            Args:
                self: current instance of that object
        """
        super(Listing, self).save(**kwargs)
        item = self.item
        item.stock = (len(Listing.objects.get_queryset().filter(
            available = True,
            item = item)))
        item.lowestCurrListing = Listing.objects.lowestCurrentPrice(item.name)['price__min']
        item.highestCurrListing = Listing.objects.highestCurrentPrice(item.name)['price__max']

        avg = Listing.objects.avgSoldPrice(item.name)['price__avg']
        if (avg == None):
            item.avgSoldPrice = 0.00
        else:
            item.avgSoldPrice = avg

        lowest =  Listing.objects.highestSoldPrice(item.name)['price__max']
        if (lowest == None):
            item.lowestSoldListing = 0.00
        else:
            item.lowestSoldListing = lowest

        highest = Listing.objects.lowestSoldPrice(item.name)['price__min']
        if(highest == None):
            item.highestSoldListing = 0.00
        else:
            item.highestSoldListing = highest

        self.updated = datetime.date.today()

        item.save()



    @property
    def item_name(self):
        return self.item.name

    @property
    def item_slug(self):
        return self.item.slug

    class Meta:
        ordering = ('-created',)
        index_together = (('id'),)
        verbose_name_plural = 'Listings'

    def delete(self):
        '''
            This function will simply just delete a listing and update everything involved within deleting a listing
        '''
        self.item.stock -= 1
        self.available = False
        self.updated = datetime.date.today()


    def get_absolute_url(self):
        # plan out views
        return reverse('shop:listing', args=[self.item.id, self.item.slug, self.id])

    def updateItemListingCreated(self):
        """
            This function will update the item model as the listing model is
            created

            Args:
                self: current instance of that object
        """
        self.item.lastActive = created
        self.item.stock += 1


    def listingSold(self):
        """
            This function will update the item object as well as the current
            instance of the listing as it has been sold. This will be called
            upon within the transaction functions

            Args:
                self: current instance of that object
        """
        self.available = False
        self.item.stock -=  1
        self.updated = datetime.date.today()

    def listingReposted(self):
        """
            This fucntion will update an item object as well
            as the listing due to being reposted due to a canceled transaction.

            Args:
                self: current instance of that object
        """
        self.available = True
        self.item.stock += 1
        updated = datetime.date.today()
        if self.price < self.item.lowestCurrListing:
            self.item.lowestCurrListing = self.price

        elif self.price > self.item.highestCurrListing:
            self.item.highestCurrentPrice = self.price

#Add a save to transactions
class Transaction(models.Model):
    """
        This is a model for listings on the exchange.

        Attributes:
            seller: A foriegn key to a user object that sold the listings
            buyer: A foreign key to a user object that is buying the listings
            amountExchanged: the amount of money exchanged between seller and
                buyer
            listing = A foreign key to the listing object to mark it as sold
            deliveryAddress = a text field which contains the address of the
                seller
            receiveAddress = a text field which contains the address of the
                buyer
            ratingSeller = a decimal field which contains a rating for the
                seller 1-5
            ratingBuyer = a decimal field which contains a rating for the buyer
                1-5
            isValid = a boolean field which stores whether the transaction
                will go through or cancel
    """
    seller = models.ForeignKey(
                settings.AUTH_USER_MODEL,
                on_delete=models.CASCADE,
                related_name='Seller'
    )
    buyer = models.ForeignKey(
                settings.AUTH_USER_MODEL,
                on_delete=models.CASCADE,
                related_name='Buyer'
    )
    amountExchanged = models.DecimalField(
                decimal_places=2,
                max_digits=10
    )
    listing = models.ForeignKey(Listing, related_name = "Listing")
    deliveryAddress = models.TextField()
    receiveAddress = models.TextField()
    timeSold = models.DateTimeField(auto_now = True)
    ratingSeller =  models.DecimalField(
            decimal_places = 1,
            max_digits = 1

    )
    ratingBuyer = models.DecimalField(
            decimal_places = 1,
            max_digits = 1

    )
    isValid = models.BooleanField(default = True)
    objects = TransactionManager()


    def save(self, **kwargs):
        """
            This function is to make the listin automatcally update the listing depending
            on the transaction

            Args:
                self: current instance of that object
        """
        super(Transaction, self).save(**kwargs)
        listing = self.listing
        if self.isValid:
            listing.available = False
            listing.save()



    def transactionMade(self):
        """
            This function will verify that a transaction has been made amd call
            upon the correct listing function to communicate this

            Args:
                self: current instance of that object
        """

        self.isValid = True
        self.listing.listingsold()
        avg = self.listing.objects.avgSoldPrice()
        item = self.listing.item
        item.avgSoldPrice = avg

    def transactionCanceled(self):
        """
            This function will verify that a transaction has been canceled and
            will call upon the correct listing function to communicate this

            Args:
                self: current instance of that object
        """
        self.isValid = False
        self.listing.listingReposted()
        avg = self.listing.objects.avgSoldPrice()
        item = self.listing.item
        item.avgSoldPrice = item['price__avg']

        if self.listing.price < self.listing.item.lowestSoldListing :
            self.listing.item.lowestSoldListing = self.listing.objects.lowestSoldPrice(
                self.listing.item.name
            )
        elif self.listing.price > self.listing.item.highestSoldListing:
            self.listing.item.highestSoldListing = self.listng.objects.highestSoldPrice(
                self.listing.item.name
            )
