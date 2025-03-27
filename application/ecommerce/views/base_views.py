from django.shortcuts import render
from ecommerce.models import Product, Category
from django.views.generic import ListView, DetailView
from django.shortcuts import redirect
# Create your views here.

PER_PAGE = 14


class ProductListView(ListView):
    model = Product
    template_name = 'ecommerce/index.html'
    paginate_by = PER_PAGE
    ordering = '-pk'
    queryset = Product.objects.filter(active=True)


class SearchProductView(ProductListView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._search_value = ''

    def setup(self, request, *args, **kwargs):
        self._search_value = request.GET.get('q', '').strip()
        return super().setup(request, *args, **kwargs)
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset =  (
            queryset.filter(
                name__icontains=self._search_value
            ).order_by('-id')
        )

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self._search_value = self.request.GET.get('q', '').strip()

        context.update(
            {
                'search_value': self._search_value,
            }
        )

        return context
    
    def get(self, request, *args, **kwargs):
        if self._search_value == '':
            return redirect('ecommerce:index')

        return super().get(request, *args, **kwargs)


def about(request):
    return render(request, 'ecommerce/about.html')


class CategoriesListView(ListView):
    model = Category
    template_name = 'ecommerce/category.html'
    context_object_name = 'categories'
    queryset = Category.objects.filter(product__active=True).all()

class CategoryProductListView(ProductListView):
    template_name = 'ecommerce/category.html'

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        return super().get_queryset().filter(category__slug=slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()

        context.update(
            {
                'categories': categories,
            }
        )
        return context

