from ecommerce.models import Order, OrderItem, ProductVariation
from django.views.generic import View
from django.contrib import messages
from django.shortcuts import render, redirect
# Create your views here.


class OrderView(View):
    template_name = 'ecommerce/detail/order_detail.html'

    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('ecommerce:login')
        
        session = self.request.session
        cart = session.get('cart')
        cart_items = [v for v in cart]
        products = list(ProductVariation.objects.select_related('produto').filter(pk__in=cart_items))

        for variation in products:
            variation_id = str(variation.pk)
            stock = variation.stock
            cart_amount = cart[variation_id]['amount']
            price = cart[variation_id]['price']
            promotional_price = cart[variation_id]['promotional_price']

            if stock < cart_amount:
                messages.error(
                    self.request,
                    f'Produto {variation.produto.name} em falta!'
                )
                return redirect('ecommerce:get_products_cart')
        

        # order = OrderItem.objects.create(
        #     ...
        # )


        context = {}

        return render(self.request, self.template_name, context)
    
