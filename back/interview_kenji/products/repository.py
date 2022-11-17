from products.models import Product


class ProductRepository:
    def get_all_products(self):
        return Product.objects.all()

    def get_products_by_category(self, category_name):
        return Product.objects.filter(category__name=category_name)
