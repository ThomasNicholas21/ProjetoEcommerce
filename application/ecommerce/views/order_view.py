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

        order = Order(
            user = self.request.user,
            total_value = sum([p.price for p in products]),  
            total_items = sum([cart[str(p.id)].get('amount') for p in products]),
            status = 'C'	

        )
        order.save()

        OrderItem.objects.bulk_create(
            [
                OrderItem(
                    pedido = order,
                    product_name = p.produto.name,
                    product_id = p.produto.id,
                    product_variation = p.name,
                    product_variation_id = p.id,
                    price = p.price,
                    product_amount = cart[str(p.id)].get('amount'),
                    imagem = p.product_image.url if p.product_image else None
                    ) for p in products
            ]
        )
        
        print(OrderItem.objects.all()  )


        context = {}

        return render(self.request, self.template_name, context)
    
