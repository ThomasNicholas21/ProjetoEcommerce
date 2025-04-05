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
        
        if not session_django.get('cart'):
            session_django.setdefault('cart', {})
            session_django.save()

        cart = session_django.get('cart')

        if variation.stock == 0:
            messages.error(
                self.request,
                'Produto em falta!'
            )
            return redirect('ecommerce:product', slug=variation.produto.slug)
        
        """
        pedido 
        product_name 
        product_id
        product_variation 
        product_variation_id
        price
        product_amount 
        imagem 
        """
        return HttpResponse(
                session_django.items()
                )
