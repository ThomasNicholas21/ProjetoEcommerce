from django.urls import path
from ecommerce.views import ProductListView, about, CategoriesListView, CategoryProductListView, ProductDetailView, SearchProductView
from ecommerce.views import UserRegisterFormView

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

    # User Views
    # User Create
    path('user/register/', UserRegisterFormView.as_view(), name='register'),
    # User Update
    path('product/<slug:slug>', ProductDetailView.as_view(), name='product'),
    # User Delete
    path('product/<slug:slug>', ProductDetailView.as_view(), name='product'),

]
