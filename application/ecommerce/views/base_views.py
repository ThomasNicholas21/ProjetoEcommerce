from django.shortcuts import render
from django.core.paginator import Paginator
from ecommerce.models import Product
# Create your views here.

PER_PAGE = 6


def index(request):
    products = Product.objects.order_by('-id').filter(active=True).all()

    paginator = Paginator(products, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj
    }

    return render(request, 'ecommerce/index.html', context)


def about(request):
    return render(request, 'ecommerce/about.html')


def category(request):
    return render(request, 'ecommerce/index.html')
