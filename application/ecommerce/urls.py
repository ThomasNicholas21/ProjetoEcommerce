from django.urls import path
from ecommerce.views import index

app_name='ecommerce'

urlpatterns = [
    path('index/', index, name='index')
]
