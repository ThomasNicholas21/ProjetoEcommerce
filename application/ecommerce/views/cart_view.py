from django.views import View
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
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

            if variation.stock < cart_amount:
                messages.warning(
                    self.request,
                    mark_safe(
                        f'Estoque do pruduto<br>'
                        f'<li>{variation.name} é insuficiente</li>'
                    )
                )
                cart_amount = variation.stock
            
            cart[variation_id]['amount'] = cart_amount
            cart[variation_id]['price'] = price * cart_amount
            cart[variation_id]['promotional_price'] = promotional_price * cart_amount


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

        self.request.session.save()

        messages.success(
            self.request,
            'Produto adicionado ao carrinho!'
        )

        return redirect(http_referer)
    