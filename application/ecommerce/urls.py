from django.urls import path
from ecommerce.views import ProductListView, about, CategoryDetailView, CategoryListView, ProductDetailView, SearchProductView

app_name='ecommerce'

urlpatterns = [
    # Base Views
    path('index/', ProductListView.as_view(), name='index'),
    path('about/', about, name='about'),
    path('category/', CategoryDetailView.as_view(), name='category'),
    path('category/<slug:slug>', CategoryListView.as_view(), name='category'),
    path('search/', SearchProductView.as_view(), name='search'),

    # Product Views
    path('product/<slug:slug>', ProductDetailView.as_view(), name='product'),
]
