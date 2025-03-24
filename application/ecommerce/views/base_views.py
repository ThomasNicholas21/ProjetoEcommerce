from django.shortcuts import render
from django.core.paginator import Paginator
from ecommerce.models import Product
from django.views.generic import ListView
from django.shortcuts import redirect
from django.db.models import Q
# Create your views here.

PER_PAGE = 12


class ProductListView(ListView):
    model = Product
    template_name = 'ecommerce/index.html'
    paginate_by = PER_PAGE
    ordering = '-pk'
    queryset = Product.objects.filter(active=True)



def about(request):
    return render(request, 'ecommerce/about.html')


def category(request):
    return render(request, 'ecommerce/category.html')
