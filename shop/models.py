from django.db import models
from django.core.urlresolvers import reverse
from django.core.validators import MaxValueValidator, MinValueValidator


class Category(models.Model):
    """
        This is a model for a predetermined list of clothing categories.

        List:
        Jackets, shirts, sweaters, sweatshirts, pants, t-shirts, hats, accessories, skate, bike, and other

        Attributes:
            name: A string of the name of a category
    """
    name = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=50, db_index=True, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('shop:item_list_by_category', args=[self.slug])


class SubCatergory(models.Model):
    """
        This is a model for a list of clothing sub-categories that are either predetermind or user input.

        Attributes:
            name: A string of the name of a sub-category
    """
    name = models.CharField(max_length=16)
    parent = models.ForeignKey(Category)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Sub Categories'

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
    """
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique = True)
    # brand = models.ForeignKey(Brand)
    description = models.TextField(blank=True)
    material = models.TextField(blank=True)
    # related_name may not be needed. Research!!!
    category = models.ForeignKey(Category, related_name='Item')
    subCatergory = models.ForeignKey(SubCatergory)
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
    lowestSoldLising = models.DecimalField(
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
    lastActive = models.DateTimeField()
    available = models.BooleanField(default = True)
    stock = models.PositiveIntegerField(
            default = 0
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-lastActive',)
        index_together = (('id','slug'),)
        verbose_name_plural = 'Items'

    def get_absolute_url(self):
        return reverse('shop:item_detail', args=[self.id, self.slug])


class Listing(models.Model):
    """
        This is a model for listings on the exchange.

        Attributes:
            name: A string of the name of the item that the listing is tied to
    """
    # seller = models.ForeignKey('settings.AUTH_USER_MODEL')
    item = models.ForeignKey(Item, related_name='Lisiting')
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

    def __str__(self):
        return self.item.name

    class Meta:
        ordering = ('-created',)
        index_together = (('id'),)
        verbose_name_plural = 'Listings'

    def get_absolute_url(self):
        # plan out views
        return reverse('shop:listing', args=[self.item.id, self.item.slug, self.id])

    def updateItem(self):
        # should update lastActive everytime a listing is created for that item
        self.item.lastActive = created
        self.item.stock += 1
