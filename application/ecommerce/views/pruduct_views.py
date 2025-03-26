from ecommerce.models import Product
from django.views.generic.detail import DetailView
import json
# Create your views here.


class ProductDetailView(DetailView):
    model = Product
    template_name = 'ecommerce/product.html'
    slug_field = 'slug'
    context_object_name = 'product'
    queryset = Product.objects.filter(active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        variations = product.productvariation_set.all()

        variation_data = [
                {
                    "id": v.id,
                    "name": v.name,
                    "price": float(v.price),
                    "promotional_price": float(v.promotional_price),
                    "image": v.product_image.url if v.product_image else product.product_image.url,
                }
                for v in variations
        ]

        context.update(
            {
                "variations_json": json.dumps(variation_data)
            }
        )
        
        return context