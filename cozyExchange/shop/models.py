from django.db import models
from django.core.urlresolvers import reverse
from django.core.validators import MaxValueValidator, MinValueValidator

class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=50, db_index=True, unique=True)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])

class Product(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    description = models.TextField(blank=True)
    material = models.TextField(blank=True)
    category = models.ForeignKey(Category, related_name='products')
    available = models.BooleanField(default=True)
    stock = models.PositiveIntegerField()
    seller = models.ForeignKey('profiles.Profile')
    conditionRating = models.FloatField(
            default=5.0,
            validators=[MaxValueValidator(10.0), MinValueValidator(1.0)]
            )
    conditionDescription = models.TextField(blank=True)
    isTeared = models.BooleanField(default = False)
    isStained = models.BooleanField(default = False)
    location = models.CharField(max_length = 50)
    price = models.DecimalField(
            default=1.00,
            validators=[MinValueValidator(1.0)],
            decimal_places=2,
            max_digits=10,
        )
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])


# class SubCatergory(models.Model):
#     name = models.CharField(max_length=16)
#     def __str__(self):
#         return self.name
#     class Meta:
#         verbose_name_plural = 'Sub Categories'

# class Brand(models.Model):
#     name = models.CharField(max_length=32)
#     description = models.TextField(blank=True)
#     location = models.CharField(max_length = 50)
#     owner = models.ForeignKey('profiles.Profile')
#     email = models.EmailField(blank=True)
#
#     def _str_(self):
#         return self.name

# class Product(models.Model):
#     name = models.CharField(max_length=200, db_index=True)
#     slug = models.SlugField(max_length=200, db_index=True)
#     description = models.TextField(blank=True)
#     material = models.TextField(blank=True)
#     category = models.ForeignKey(Category, related_name='products')
#     available = models.BooleanField(default=True)
#     stock = models.PositiveIntegerField()
#     avgPrice = models.FloatField(default=0.0)
#     lowestCurrListing = models.FloatField()
#     highestCurrListing = models.FloatField()
#     lowestHistLising = models.FloatField()
#     highestHistListing = models.FloatField()
#     subCatergory = models.ForeignKey(SubCatergory)
#     brand = models.ForeignKey(Brand)
#
#     def __str__(self):
#         return self.name
#     class Meta:
#         verbose_name_plural = 'Products'
#
# class Listing(models.Model):
#     seller = models.ForeignKey('profiles.Profile')
#     product = models.ForeignKey(
#         Product,
#         null=True)
#     conditionRating = models.FloatField(
#         default=5.0,
#         validators=[MaxValueValidator(10.0), MinValueValidator(1.0)]
#         )
#     conditionDescription = models.TextField(blank=True)
#     isTeared = models.BooleanField(default = False)
#     isStained = models.BooleanField(default = False)
#     location = models.CharField(max_length = 50)
#     price = models.DecimalField(
#         default=1.00,
#         validators=[MinValueValidator(1.0)],
#         decimal_places=2,
#         max_digits=10,
#     )
#     available = models.BooleanField(default=True)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.product.name
