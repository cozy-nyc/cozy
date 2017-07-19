from shop.models import Category, SubCatergory, Item, Listing
from django.db.models.manager import Manager
from django.db.models import Min, Avg, Max
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
    def avgSoldPrice(self,itemRef):
        """
            This function will run a query that will return the average price
            that a paticular item has been sold for.

            Args:
                self: current instance of that object
                itemRef: the reference to the item we wish to find the average
                    selling price of

            Return: An float that contains the average sold price of a
                        particular item
        """
        return self.filter(
            item = itemRef,
            available = False
            ).aggregate(Avg('price'))

    def lowestSoldPrice(self, itemRef):
        """
            This function will run a query that will return the lowest price
            that a paticular item has been sold for.

            Args:
                self: current instance of that object
                itemRef: the reference to the item we wish to find the lowest
                    sold price of

            Return: An float that contains the lowest sold price of a
                        particular item
        """
        return self.filter(
            item = itemRef,
            available = False
            ).aggregate(Min('price'))

    def highestSoldPrice(self, itemRef):
        """
            This function will run a query that will return the highest price
            that a paticular item has been sold for.

            Args:
                self: current instance of that object
                itemRef: the reference to the item we wish to find the highest
                    selling price of

            Return: An float that contains the lowest sold price of a
                        particular item
        """
        return self.filter(
            item = itemRef,
            available = False
            ).aggregate(Max('price'))

    def lowestCurrentPrice(self):
        """
            This function will run a query that will return the lowest price
            that is currently listed

            Args:
                self: current instance of that object
                itemRef: the reference to the item we wish to find the lowest
                            current listing price

            Return: An float that contains the lowest current listing price of
                        a particular item
        """
        return self.filter(
            item = itemRef,
            available = True
            ).aggregate(Min('price'))

    def highestCurrentPrice(self):
        """
            This function will run a query that will return the highest price
            that is currently listed

            Args:
                self: current instance of that object
                itemRef: the reference to the item we wish to find the highest
                            current listing price

            Return: An float that contains the highest current listing price of
                        a particular item
        """
        return self.filter(
            item = itemRef,
            available = True
            ).aggregate(Max('price'))

class TransactionManager(Manager):
