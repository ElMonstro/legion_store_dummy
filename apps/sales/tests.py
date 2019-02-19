from django.test import TestCase

from .factories import (CategoryFactory, ProductFactory, SaleFactory,
                        SaleItemFactory, UserFactory)


class CategoryModelTests(TestCase):

    def setUp(self):
        self._category = CategoryFactory.create()


    def test_category_string_representation(self):
        self.assertEqual(str(self._category), self._category.title)


class ProductModelTests(TestCase):

    def setUp(self):
        self._category1 = CategoryFactory.create()
        self._product1 = ProductFactory.create(category=self._category1)

    def test_product_string_represenation(self):
        self.assertEqual(str(self._product1), self._product1.name)


class SaleModelTests(TestCase):

    def setUp(self):
        self._category1 = CategoryFactory.create()
        self._product1 = ProductFactory.create(category=self._category1)
        self._user = UserFactory.create()
        self._sale = SaleFactory.create(attendant=self._user)
