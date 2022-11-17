from django.http import HttpResponse
from django.views import View
from django.core import serializers


from products.repository import ProductRepository


class ProductsViews(View):
    repository = ProductRepository()

    def get(self, request, *args, **kwargs):
        category_name = kwargs.get('category')

        if category_name:
            queryset = self.repository.get_products_by_category(category_name)
        else:
            queryset = self.repository.get_all_products()

        qs_json = serializers.serialize('json', queryset)
        return HttpResponse(qs_json, content_type='application/json')
