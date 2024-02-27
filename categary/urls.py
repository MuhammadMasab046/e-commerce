from django.urls import path
from .views import add_categary_view, render_index_page, add_product_view, render_cart_view, render_checkout_view

from django.urls import include, path
from rest_framework import routers
from .views import CategaryViewSet, ProductViewSet, CartViewSet, BillingViewSet, OrderViewSet

router = routers.DefaultRouter()

router.register(r'categary', CategaryViewSet, basename="Categary")
router.register(r'products', ProductViewSet, basename="Products")
router.register(r'carts', CartViewSet, basename="Carts")
router.register(r'bill', BillingViewSet, basename="Billing")
router.register(r'order', OrderViewSet, basename="Orders")
#path('products/by_category/', ProductViewSet.as_view({'get': 'products_by_category'}), name='products-by-category'),

urlpatterns = [
    path('categary/create/', add_categary_view, name='add_categary_view'),
    path('product/create/', add_product_view, name='add_product_view'),
    path('categary/index/', render_index_page, name='index_page'),
    path('categary/cart/', render_cart_view, name='cart_page'),
    path('categary/checkout/', render_checkout_view, name='checkout_page'),
    path('', include(router.urls)),
]



# urlpatterns = [
#     # Your URL patterns go here
#     path('create/', add_categary_view, name='add_categary_view'),
# ]