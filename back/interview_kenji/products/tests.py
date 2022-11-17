from django.test import TestCase

from products.repository import ProductRepository
from products.models import Product, Category


class Products(TestCase):
    def setUp(self):
        category_electro = Category.objects.create(name="Electrodomesticos")
        category_limpieza = Category.objects.create(name="Limpieza")
        Product.objects.create(name="heladera", category=category_electro, price="200000", stock=100)
        Product.objects.create(name="lavarropa", category=category_electro, price="200000", stock=100)
        Product.objects.create(name="microondas", category=category_electro, price="200000", stock=100)
        Product.objects.create(name="escoba", category=category_limpieza, price="200", stock=100)

    def test_repository_returns_all_products(self):
        products = ProductRepository().get_all_products()
        self.assertEqual(products.count(), 4)

    def test_repository_returns_products_by_category(self):
        products = ProductRepository().get_products_by_category('Limpieza')
        self.assertEqual(products.count(), 1)
