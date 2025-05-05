from django.views import View
from django.views.generic import TemplateView
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.utils.safestring import mark_safe
from ..models import ProductVariation, Order
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

        if not variation_id or not variation_id.isdigit():
            messages.error(self.request, 'Produto inválido!')
            return redirect(http_referer)

        session = self.request.session
        cart = session.get('cart', {})
        variation = get_object_or_404(ProductVariation, pk=variation_id)
        produto = variation.produto
        stock = variation.stock
        product_name = produto.name

        if variation_id not in cart:
            messages.error(self.request, 'Produto não está no carrinho!')
            return redirect(http_referer)

        cart_amount = cart[variation_id].get('amount')
        unit_price = cart[variation_id]['price'] / cart_amount
        unit_promo_price = cart[variation_id]['promotional_price'] / cart_amount

        if action == 'increase':
            if stock <= cart_amount:
                messages.warning(
                    self.request,
                    mark_safe(
                        f'Estoque insuficiente para {cart_amount + 1}x no produto "{product_name}". '
                        f'Adicionamos {stock}x no seu carrinho.'
                    )
                )
                cart[variation_id]['amount'] = stock
                cart[variation_id]['price'] = unit_price * stock
                cart[variation_id]['promotional_price'] = unit_promo_price * stock

            else:
                cart[variation_id]['amount'] = cart_amount + 1
                cart[variation_id]['price'] = unit_price * (cart_amount + 1)
                cart[variation_id]['promotional_price'] = unit_promo_price * (cart_amount + 1)

        elif action == 'decrease':
            if cart_amount == 1:
                del cart[variation_id]
                messages.success(self.request, 'Produto excluído do seu carrinho!')

                if session.get('order') and not cart:
                    order_id = session['order'].get('id')
                    Order.objects.filter(id=order_id).delete()
                    session.pop('order', None)
            else:
                cart[variation_id]['amount'] = cart_amount - 1
                cart[variation_id]['price'] = unit_price * (cart_amount - 1)
                cart[variation_id]['promotional_price'] = unit_promo_price * (cart_amount - 1)

        session['cart'] = cart
        session.save()

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

        session_django = self.request.session

        session_django.save()

        if session_django['order']:
            if len(session_django['cart']) == 0 and session_django['order']:
                order_id = session_django['order'].get('id')
                Order.objects.filter(id=order_id).delete()
                del session_django['order']

        return redirect(http_referer)
