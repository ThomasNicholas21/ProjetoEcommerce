from django.urls import path
from ecommerce.views import ProductListView, AboutView, CategoriesListView, CategoryProductListView, ProductDetailView, SearchProductView
from ecommerce.views import UserRegisterFormView, AuthenticationLoginFormView, LogoutView, UserUpdateFormView
from ecommerce.views import AddVariationCartView

app_name='ecommerce'

urlpatterns = [
    # Base Views
    path('index/', ProductListView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('categories/', CategoriesListView.as_view(), name='categories'),
    path('category/<slug:slug>/', CategoryProductListView.as_view(), name='category'),
    path('search/', SearchProductView.as_view(), name='search'),

    # Product Views
    path('product/<slug:slug>', ProductDetailView.as_view(), name='product'),

    # Carrinho
    path('add_compose_product_cart/', AddVariationCartView.as_view(), name='post_compose_product_cart'),
    #path('add_simple_product_cart/', AddVariationCartView.as_view(), name='post_simple_product_cart'),

    # User Views
    path('user/login/', AuthenticationLoginFormView.as_view(), name='login'),
    path('user/logout/', LogoutView.as_view(), name='logout'),
    path('user/register/', UserRegisterFormView.as_view(), name='register_user'),
    path('user/update/', UserUpdateFormView.as_view(), name='update_user'),

]
