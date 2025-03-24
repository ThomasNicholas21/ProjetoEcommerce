from django.shortcuts import render
from ecommerce.models import Product
# Create your views here.


def product_view(request, product_slug):
    return render(request)