from django.views import View
from django.http import HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from ..models import ProductVariation
# Create your views here.


class AddCartView(View):
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
        
        if produto.product_type == "S":
            if produto.promotional_price:
                price = produto.promotional_price
            else:
                price = produto.price
        
        elif produto.product_type == "V":
            if variation.promotional_price:
                price = variation.promotional_price
            else:
                price = variation.price
        
        amount = 1
        slug = produto.slug

        if produto.product_type == "S":
            imagem = produto.product_image.name
        
        elif produto.product_type == "V":
            imagem = variation.product_image.name

        if not session_django.get('cart'):
            session_django.setdefault('cart', {})
            session_django.save()

        cart = session_django.get('cart')

        if variation_id in cart:
            pass
        else:
            cart.setdefault(
                    variation_id,
                    {
                        'product_name': product_name,
                        'product_id': product_id,
                        'product_variation': product_variation,
                        'product_variation_id': product_variation_id,
                        'price': float(price),
                        'amount': amount,
                        'product_slug': slug,
                        'imagem': imagem,
                    }
                )

        self.request.session.save()

        return HttpResponse(
                session_django.items()
                )
