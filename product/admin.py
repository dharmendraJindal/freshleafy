from django.contrib import admin

from product.models import Product
from product.models import ProductCategory


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(ProductCategory, ProductCategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display    = ('name', 'grade', 'image_path')
    list_filter = ["name", "grade"]


admin.site.register(Product, ProductAdmin)
