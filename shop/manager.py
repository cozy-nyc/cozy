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
    def siblings(self, catName):
        return self.get_queryset().filter(parent = catName)


class ItemManager(Manager):
    """
    This is a manager for Items where we can store commonly used querysets as
    well as functions that will be used in our django project
    """

    def newItem(self,name, description, material, category, subCategory):
        item = self.model(name = name,
        description = description,
        material = material,
        category = category,
        subCategory = subCategory,
        lastActive = datetime.date.today()
        )

    def findItem(self, name = None , category = None  , subCategory = None):
        if name != None and category != None and subCategory != None:
            return self.get_queryset().filter(name__contains = name,
            category = category,
            subCategory = subCategory
            )
        elif name != None and category != None:
            return self.get_queryset().filter(name__contains = name,
            category = categroy
            )
        elif category != None and subCategory != None:
            return self.get_queryset().filter(category = category,
            subCategory = subCategory
            )
        elif name != None:
            return self.get_queryset().filter(name__contains = name)

        elif category != None:
            return self.sharedCategory(categor.namey)

        else:
            return None




     def sharedCategory(self, catName):
        return self.get_queryset().filter(category = catName)

    def sharedSubCategory(self, subCatName):
        return self.get_queryset().filter(subCategory = subCatName)



class ListingManager(Manager):
    """
    This is a manager for Listings where we can store commonly used querysets
    as well as functions that will be used in our django project
    """

    def newListing(self,seller, item, conditionRating, description, location, price, size, available):

        listing = self.model(seller = seller,
        item = item,
        conditionRating = conditionRating,
        description = description,
        location = location,
        price = price,
        size = size,
        available = available,
        created = datetime.date.today()
        updated = datetime.date.today()
        )

        listing.save(using=self._db)

        return listing

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

    def lowestCurrentPrice(self, itemRef):
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

    def highestCurrentPrice(self, itemRef):
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
    """
    This is a manager for Transactions where we can store commonly used querysets
    as well as functions that will be used in our django project
    """
