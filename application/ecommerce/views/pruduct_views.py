from ecommerce.models import Product
from django.views.generic.detail import DetailView
# Create your views here.


class ProductDetailView(DetailView):
    model = Product
    template_name = 'ecommerce/product.html'
    slug_field = 'slug'
    context_object_name = 'product'
    queryset = Product.objects.filter(active=True)
