from django.contrib import admin

from product.models import Product
from product.models import ProductCategory
from product.models import UserOrder
from product.models import OrderedProduct


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(ProductCategory, ProductCategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'grade', 'image_path', 'rate', 'unit','is_active')
    list_filter = ["name", "grade", 'unit']


admin.site.register(Product, ProductAdmin)


class OrderedProductAdmin(admin.ModelAdmin):
    list_display = ('product', 'user_name','user_email',  'order_timestamp', 'rate', 'quantity', 'unit')
    list_filter = ['product', 'user_order__order_timestamp']


admin.site.register(OrderedProduct, OrderedProductAdmin)


class UserOrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'order_timestamp')


admin.site.register(UserOrder, UserOrderAdmin)
