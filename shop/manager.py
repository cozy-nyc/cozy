from shop.models import Category, SubCatergory, Item, Listing
from django.db.models.manager import Manager
import datetime


class CategoryManager(Manager):
    """
    This is a manager for Categories where we can store commonly used querysets
    that will be used in our django project

    """


class SubCatergoryManager(Manager):
    """
    This is a manager for SubCategories where we can store commonly used
    querysets that will be used in our django project
    """
    def parents(self, catName):
        return self.get_queryset().filter(parent = catName)


class ItemManager(Manager):
    """
    This is a manager for Items where we can store commonly used querysets as
    well as functions that will be used in our django project
    """

     def sharedCategory(self, catName):
        return self.get_queryset().filter(category = catName)

    def sharedSubCategory(self, subCatName):
        return self.get_queryset().filter(subCategory = subCatName)



class ListingManager(Manager):
    """
    This is a manager for Listings where we can store commonly used querysets
    as well as functions that will be used in our django project
    """
