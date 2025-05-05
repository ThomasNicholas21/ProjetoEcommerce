from ecommerce.models import Order, OrderItem, ProductVariation
from django.views.generic import View
from django.contrib import messages
from django.shortcuts import render, redirect
from utils.slug.slug_gen import new_slug
# Create your views here.

class OrderCreateView(View):
    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('ecommerce:login')
        
        session = self.request.session
        cart = session.get('cart')
        order = session.get('order')
        cart_items = [v for v in cart]
        products = list(ProductVariation.objects.select_related('produto').filter(pk__in=cart_items))

        if not cart:
            messages.error(
                self.request,
                'Carrinho vazio!'
            )
            return redirect('ecommerce:index')
            
        order = Order(
            user = self.request.user,
            slug = new_slug(self.request.user, 5),
            total_value = sum(
                [
                    p.promotional_price * cart[str(p.id)].get('amount') 
                    if p.promotional_price != 0
                    else p.price * cart[str(p.id)].get('amount')
                    for p in products
                ]
            ),
            total_items = sum(
                [
                    cart[str(p.id)].get('amount') for p in products
                ]
            ),
            status = 'O'	

        )
        order.save()
        
        OrderItem.objects.bulk_create(
            [
                OrderItem(
                    pedido = order,
                    product_name = p.produto.name,
                    slug = new_slug(p.produto.name, 5),
                    product_id = p.produto.id,
                    product_variation = p.name,
                    product_variation_id = p.id,
                    price = (
                        p.promotional_price * cart[str(p.id)].get('amount') 
                        if p.promotional_price != 0   
                        else p.price * cart[str(p.id)].get('amount')
                        ),
                    product_amount = cart[str(p.id)].get('amount'),
                    imagem = p.product_image.url if p.product_image else None
                    ) for p in products
            ]
        )

        created_order = Order.objects.order_by('-pk').first()
        session['order'] = {
                                'slug': created_order.slug,
                                'id': created_order.id
                            }

        if OrderItem.objects.filter(pedido=order).exists():
            messages.success(
                self.request,
                'Pedido criado com sucesso!'
            )

            return redirect('ecommerce:order_detail', order_id=order.id)
        
        messages.error(
            self.request,
            'Erro ao realizar o pedido! Entre em contato com o suporte!'
        )

        return redirect('ecommerce:get_products_cart')
    

class OrderAlterView(View):
    def get(self, *args, **kwargs):
        session = self.request.session
        cart = session.get('cart')
        order = session.get('order')
        cart_items = [v for v in cart]

        if order:
            order_slug = order.get('slug')
            order = Order.objects.filter(slug=order_slug).first()
            new_products = (
                list(ProductVariation.objects
                .filter(pk__in=cart_items)
                .exclude(id__in=
                            [
                                p.product_variation_id 
                                for p in OrderItem.objects.filter(pedido__slug=order_slug)
                            ]
                        ))
                    )
            
            update_products = list(OrderItem.objects.filter(pedido=order))

            for item in update_products:
                amount = cart[str(item.product_variation_id)]['amount']
                
                old_amount = item.product_amount or 1  
                unit_price = item.price / old_amount

                item.product_amount = amount
                item.price = unit_price * amount
            
            OrderItem.objects.bulk_update(
                update_products,
                ['product_amount', 'price']
            )
            
            OrderItem.objects.bulk_create(
                [
                    OrderItem(
                        pedido = order,
                        product_name = p.produto.name,
                        slug = new_slug(p.produto.name, 5),
                        product_id = p.produto.id,
                        product_variation = p.name,
                        product_variation_id = p.id,
                        price = (
                            p.promotional_price * cart[str(p.id)].get('amount') 
                            if p.promotional_price != 0   
                            else p.price * cart[str(p.id)].get('amount')
                            ),
                        product_amount = cart[str(p.id)].get('amount'),
                        imagem = p.product_image.url if p.product_image else None
                    ) for p in new_products
                ]
            )

        return redirect('ecommerce:order_detail', order_id=order.id)

class OrderDetailView(View):
    template_name = 'ecommerce/detail/order_detail.html'

    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('ecommerce:login')
        
        order_id = kwargs.get('order_id')
        order = Order.objects.filter(pk=order_id).first()

        context = {
            'order': order,
            'order_items': OrderItem.objects.filter(pedido=order_id),
        }

        return render(self.request, self.template_name, context)
