from django.urls import path
from ecommerce.views import index, about, category, ProductDetailView

app_name='ecommerce'

urlpatterns = [
    # Base Views
    path('index/', index, name='index'),
    path('about/', about, name='about'),
    path('category/', category, name='category'),

    # Product Views
    path('product/<slug:slug>', ProductDetailView.as_view(), name='product'),
]
