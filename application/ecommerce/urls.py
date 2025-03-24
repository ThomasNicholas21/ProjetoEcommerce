from django.urls import path
from ecommerce.views import index, about

app_name='ecommerce'

urlpatterns = [
    path('index/', index, name='index'),
    path('about/', about, name='about'),
    path('category/', about, name='category'),
]
