from django.contrib import admin
from .models import categary, products, cart

# Register your models here.

@admin.register(categary)
class CategaryAdmin(admin.ModelAdmin):
    pass

@admin.register(products)
class ProductsAdmin(admin.ModelAdmin):
    pass

@admin.register(cart)
class CartsAdmin(admin.ModelAdmin):
    pass

# @admin.register(cartItem)
# class CartsItemAdmin(admin.ModelAdmin):
#     pass
