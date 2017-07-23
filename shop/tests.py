from django.test import TestCase
from .models import Category, SubCategory, Item, Listing, Transaction
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
