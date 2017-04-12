from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Categories'

class SubCatergory(models.Model):
    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Sub Categories'

class Brand(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField()
    location = models.TextField()
    owner = models.TextField()
    email = models.TextField()

    def _str_(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField()
    material = models.TextField()
    avgPrice = models.FloatField()
    lowestCurrListing = models.FloatField()
    highestCurrListing = models.FloatField()
    lowestHistLising = models.FloatField()
    highestHistListing = models.FloatField()
    category = models.ForeignKey(Category)
    subCatergory = models.ForeignKey(SubCatergory)
    brand = models.ForeignKey(Brand)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Products'

class Listing(models.Model):

    seller = models.ForeignKey('profiles.Profile')
    # product = models.ForeignKey(Product)
    conditionRating = models.FloatField()
    conditionDescription = models.TextField()
    status = models.TextField()
    isTeared = models.BooleanField()
    isStained = models.BooleanField()
    location = models.TextField()
    price = models.BooleanField()
