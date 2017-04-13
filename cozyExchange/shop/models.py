from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Category(models.Model):
    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Categories'

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

class Product(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(blank=True)
    material = models.TextField(blank=True)
    # avgPrice = models.FloatField(default=0.0)
    # lowestCurrListing = models.FloatField()
    # highestCurrListing = models.FloatField()
    # lowestHistLising = models.FloatField()
    # highestHistListing = models.FloatField()
    category = models.ForeignKey(Category)
    # subCatergory = models.ForeignKey(SubCatergory)
    # brand = models.ForeignKey(Brand)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Products'

class Listing(models.Model):
    seller = models.ForeignKey('profiles.Profile')
    product = models.ForeignKey(
        Product,
        null=True)
    conditionRating = models.FloatField(
        default=5.0,
        validators=[MaxValueValidator(10.0), MinValueValidator(1.0)]
        )
    conditionDescription = models.TextField(blank=True)
    isTeared = models.BooleanField(default = False)
    isStained = models.BooleanField(default = False)
    location = models.CharField(max_length = 50)
    price = models.FloatField(default=0.0)

    def __str__(self):
        return self.product.name
