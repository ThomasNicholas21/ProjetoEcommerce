from ecommerce.models import Order, OrderItem
from django.views.generic import TemplateView
from django.shortcuts import redirect
# Create your views here.


class OrderView(TemplateView):
    template_name = 'ecommerce/detail/order_detail.html'
