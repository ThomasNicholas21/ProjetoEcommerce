from django.views import View
from django.views.generic import TemplateView
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse
from pprint import pprint
from django.utils.safestring import mark_safe
from ..models import ProductVariation
# Create your views here.


class AddVariationCartView(View):
    def get(self, *args, **kwargs):
        http_referer = self.request.META.get('HTTP_REFERER', reverse('ecommerce:index'))
        variation_id = self.request.GET.get('variation_id')
        session_django = self.request.session

        if not variation_id:
            messages.error(
                self.request,
                'Produto Inexistente!'
            )
            return redirect(http_referer)
        
        if not variation_id.isdigit():
            messages.error(
                self.request,
                'Selecione um produto!'
            )
            return redirect(http_referer)
        
        variation = get_object_or_404(ProductVariation, pk=variation_id)

        if variation.stock < 1:
            messages.error(
                self.request,
                'Produto em falta!'
            )
            return redirect('ecommerce:product', slug=variation.produto.slug)

        produto = variation.produto
        stock = variation.stock
        product_name = produto.name
        product_id = produto.pk
        product_variation = variation.name
        product_variation_id = variation.pk
        price = float(variation.price)
        promotional_price = float(variation.promotional_price)
        amount = 1
        slug = produto.slug
        imagem = variation.product_image.name

        if not session_django.get('cart'):
            session_django.setdefault('cart', {})
            session_django.save()

        cart = session_django.get('cart')


        if variation_id in cart:
            cart_amount = cart[variation_id].get('amount')
            cart_amount += 1

            if stock < cart_amount:
                messages.warning(
                    self.request,
                    mark_safe(
                        f'Estoque insuficiente para {cart_amount}x no '
                        f'produto "{product_name}". Adicionamos {stock}x '
                        f'no seu carrinho.'
                    )
                )
                cart_amount = variation.stock

            else:
                cart[variation_id]['amount'] = cart_amount
                cart[variation_id]['price'] = price * cart_amount
                cart[variation_id]['promotional_price'] = promotional_price * cart_amount

                messages.success(
                    self.request,
                    'Produto adicionado ao carrinho!'
                )



        else:
            cart.setdefault(
                    variation_id,
                    {
                        'product_name': product_name,
                        'product_id': product_id,
                        'product_variation': product_variation,
                        'product_variation_id': product_variation_id,
                        'price': price,
                        'promotional_price': promotional_price,
                        'amount': amount,
                        'product_slug': slug,
                        'imagem': imagem,
                    }
                )
            messages.success(
                self.request,
                'Produto adicionado ao carrinho!'
            )

        self.request.session.save()

        return redirect(http_referer)
    

class CartView(TemplateView):
    template_name = 'ecommerce/detail/cart.html'


class AlterProductUnitCart(View):
    def get(self, *args, **kwargs):
        http_referer = self.request.META.get('HTTP_REFERER', reverse('ecommerce:index'))
        variation_id = self.request.GET.get('variation_id')
        action = self.request.GET.get('action')

        if not variation_id:
            messages.error(
                self.request,
                'Produto Inexistente!'
            )
            return redirect(http_referer)
        
        if not variation_id.isdigit():
            messages.error(
                self.request,
                'Selecione um produto!'
            )
            return redirect(http_referer)
        
        cart = self.request.session['cart']
        variation = get_object_or_404(ProductVariation, pk=variation_id)
        produto = variation.produto
        stock = variation.stock
        product_name = produto.name

        if variation_id not in cart:
            messages.error(
                self.request,
                'Produto não está no carrinho!'
            )
            return redirect(http_referer)

        cart_amount = cart[variation_id].get('amount')
        unit_price = cart[variation_id]['price'] / cart_amount
        unit_promotional_price = cart[variation_id]['promotional_price'] / cart_amount
        total_price = cart[variation_id]['price']
        total_promotional_price = cart[variation_id]['promotional_price'] 

        if action == 'increase': 
            if variation.stock <= cart_amount:
                messages.warning(
                    self.request,
                    mark_safe(
                        f'Estoque insuficiente para {cart_amount + 1}x no '
                        f'produto "{product_name}". Adicionamos {stock}x '
                        f'no seu carrinho.'
                    )
                )
                cart_amount = variation.stock

            else:
                cart_amount += 1
                cart[variation_id]['amount'] = cart_amount
                cart[variation_id]['price'] = total_price + unit_price
                cart[variation_id]['promotional_price'] = total_promotional_price + unit_promotional_price

        elif action == 'decrease':
            if cart_amount == 1:
                messages.success(
                        self.request,
                        'Produto excluido do seu carrinho!'
                    )
                del self.request.session['cart'][variation_id]

            else:
                cart_amount -= 1
                cart[variation_id]['amount'] = cart_amount
                cart[variation_id]['price'] = total_price - unit_price
                cart[variation_id]['promotional_price'] = total_promotional_price - unit_promotional_price

        self.request.session.save()

        return redirect(http_referer)
    
    
class DeleteProductView(View):
    def get(self, *args, **kwargs):
        http_referer = self.request.META.get('HTTP_REFERER', reverse('ecommerce:index'))
        variation_id = self.request.GET.get('variation_id')
        action = self.request.GET.get('action')

        if not variation_id:
            messages.error(
                self.request,
                'Produto Inexistente!'
            )
            return redirect(http_referer)
        
        if not variation_id.isdigit():
            messages.error(
                self.request,
                'Selecione um produto!'
            )
            return redirect(http_referer)
        
        cart = self.request.session['cart']

        if variation_id not in cart:
            messages.error(
                self.request,
                'Produto não está no carrinho!'
            )
            return redirect(http_referer)


        del self.request.session['cart'][variation_id]

        messages.success(
            self.request,
            'Produto excluido do seu carrinho!'
        )

        self.request.session.save()

        return redirect(http_referer)
