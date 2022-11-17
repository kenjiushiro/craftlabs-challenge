from django.contrib import admin
from django.urls import path, include

from products.views import ProductsViews


urlpatterns = [
    path('', ProductsViews.as_view()),
    path('category/<category>', ProductsViews.as_view()),
]
