from django.urls import path
from ecommerce.views import ProductListView, AboutView, CategoriesListView, CategoryProductListView, ProductDetailView, SearchProductView
from ecommerce.views import UserRegisterFormView, AuthenticationLoginFormView, LogoutView, UserUpdateFormView
from ecommerce.views import AddVariationCartView, CartView, AlterProductUnitCart, DeleteProductView
from ecommerce.views import ProfileUserFormView
from ecommerce.views import OrderView


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
    path('add_product_cart/', AddVariationCartView.as_view(), name='post_product_cart'),
    path('get_products_cart/', CartView.as_view(), name='get_products_cart'),
    path('alter_product_cart/', AlterProductUnitCart.as_view(), name='alter_product_unit_cart'),
    path('delete_product_cart/', DeleteProductView.as_view(), name='delete_product_cart'),


    # User Views
    path('user/login/', AuthenticationLoginFormView.as_view(), name='login'),
    path('user/logout/', LogoutView.as_view(), name='logout'),
    path('user/register/', UserRegisterFormView.as_view(), name='register_user'),
    path('user/update/', UserUpdateFormView.as_view(), name='update_user'),

    # Profile Views
    path('user/profile/register/', ProfileUserFormView.as_view(), name='profile_user'),

    # Order Views
    path('user/orders/', OrderView.as_view(), name='order'),
]
