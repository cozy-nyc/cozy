from django.test import TestCase
from .models import Category, SubCategory, Item, Listing, Transaction
from cuser.models import User

# Create your tests here.

class CategoryTestCase(TestCase):
    def setUp(self):
        Category.objects.create(name = "Shirts",slug = "shirts")

    def test_category_exists(self):
        shirts = Category.objects.get(name = "Shirts")
        self.assertEqual(shirts.name, 'Shirts')


class SubCategoryCase(TestCase):
    def setUp(self):
        Category.objects.create(name = "Shirts",slug = "shirts")

        SubCategory.objects.create(name = "Tank Tops",
        parent = Category.objects.get(name = "Shirts")
        )
        SubCategory.objects.create(name = "T-Shirts",
        parent = Category.objects.get(name = "Shirts")
        )

    def test_sibling(self):
        subcats = SubCategory.objects.siblings('Shirts')
        self.assertEqual(len(subcats),2)

class ItemTestCase(TestCase):
    def setUp(self):
        Category.objects.create(name = "Shirts",slug = "shirts")

        SubCategory.objects.create(name = "Tank Tops",
        parent = Category.objects.get(name = "Shirts")
        )

        SubCategory.objects.create(name = "T-Shirts",
        parent = Category.objects.get(name = "Shirts")
        )

        Item.objects.newItem(name = 'Supreme Yankee Box Logo T-Shirt White',
        description = """Supreme's collaboration with the New York Yankee in
        SS2015 resulted in production of this shirt """,
        material = "100%% Cotton",
        category = Category.objects.get(name = "Shirts"),
        subCategory = SubCategory.objects.get(name="T-Shirts")
        )

        Item.objects.newItem(name = 'Supreme Pink Tank Top',
        description = """Supreme's Tank Top from SS2017 """,
        material = "100%% Cotton",
        category = Category.objects.get(name = "Shirts"),
        subCategory = SubCategory.objects.get(name="Tank Tops")
        )


    def test_find_one(self):
        item = Item.objects.findItem(name = 'Tank Top')
        self.assertEqual(len(item), 1)

    def test_find_two(self):
        item = Item.objects.findItem(category = "Shirts")
        self.assertEqual(len(item),2)

    def test_find_three(self):
        item = Item.objects.findItem(name = 'Yankee', subCategory = 'T-Shirts')
        self.assertEqual(len(item),1)


class ListingTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='john',
        email='jlennon@beatles.com',
        password='glassonion'
        )

        user = User.objects.create_user(username='zahi',
        email='zahi@benballer.com',
        password='playboicarti'
        )

        Category.objects.create(name = "Shirts",slug = "shirts")

        SubCategory.objects.create(name = "Tank Tops",
        parent = Category.objects.get(name = "Shirts")
        )

        SubCategory.objects.create(name = "T-Shirts",
        parent = Category.objects.get(name = "Shirts")
        )

        Item.objects.newItem(name = 'Supreme Yankee Box Logo T-Shirt White',
        description = """Supreme's collaboration with the New York Yankee in
        SS2015 resulted in production of this shirt """,
        material = "100%% Cotton",
        category = Category.objects.get(name = "Shirts"),
        subCategory = SubCategory.objects.get(name="T-Shirts")
        )

        Item.objects.newItem(name = 'Supreme Pink Tank Top',
        description = """Supreme's Tank Top from SS2017 """,
        material = "100%% Cotton",
        category = Category.objects.get(name = "Shirts"),
        subCategory = SubCategory.objects.get(name="Tank Tops")
        )

        Listing.objects.newListing(
        seller = User.objects.get(username = 'zahi'),
        item = Item.objects.get(name = 'Supreme Yankee Box Logo T-Shirt White'),
        conditionRating = 4.0,
        description = "In Good Condition. No Rips",
        location = 'Queens',
        price = 200.00,
        size = "M"
        )

        Listing.objects.newListing(
        seller = User.objects.get(username = 'john'),
        item = Item.objects.get(name = 'Supreme Yankee Box Logo T-Shirt White'),
        conditionRating = 3.0,
        description = "In Good Condition. Some stains",
        location = 'Queens',
        price = 70.00,
        size = "L"
        )

        Listing.objects.newListing(
        seller = User.objects.get(username = 'zahi'),
        item = Item.objects.get(name = 'Supreme Pink Tank Top'),
        conditionRating = 3.0,
        description = "In Good Condition. Some stains",
        location = 'Queens',
        price = 50.00,
        size = "S"
        )

    def test_lowest_current_price(self):
        lowestPrice = Listing.objects.lowestCurrentPrice(
        itemRef = 'Supreme Yankee Box Logo T-Shirt White'
        )
        self.assertEqual(lowestPrice['price__min'],70.00)

        item = Item.objects.get(name = 'Supreme Yankee Box Logo T-Shirt White')
        self.assertEqual(item.lowestCurrListing, 70.00)


    def test_highest_current_price(self):
        highestPrice = Listing.objects.highestCurrentPrice(
        itemRef = 'Supreme Yankee Box Logo T-Shirt White'
        )
        self.assertEqual(highestPrice['price__max'],200.00)

        item = Item.objects.get(name = 'Supreme Yankee Box Logo T-Shirt White')
        self.assertEqual(item.highestCurrListing, 200.00)
