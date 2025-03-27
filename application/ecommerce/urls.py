from django.urls import path
from ecommerce.views import ProductListView, about, CategoriesListView, CategoryProductListView, ProductDetailView, SearchProductView

app_name='ecommerce'

urlpatterns = [
    # Base Views
    path('index/', ProductListView.as_view(), name='index'),
    path('about/', about, name='about'),
    path('categories/', CategoriesListView.as_view(), name='categories'),
    path('category/<slug:slug>/', CategoryProductListView.as_view(), name='category'),
    path('search/', SearchProductView.as_view(), name='search'),

    # Product Views
    path('product/<slug:slug>', ProductDetailView.as_view(), name='product'),
]
