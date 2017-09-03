from rest_framework import serializers

from product.models import Product
from product.models.RateUnit import RateUnit
from product.serialisers.ProductCategorySerialiser import ProductCategorySerializer


class ProductSerialiser(serializers.ModelSerializer):
    product_category = ProductCategorySerializer(many=True)
    product_id = serializers.SerializerMethodField()
    hindi_name = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('name','hindi_name' ,'image_path','product_category', 'grade', 'rate', 'unit', 'product_id')

    def get_product_id(self, obj):
        return obj.id

    def get_hindi_name(self, obj):
        return obj.name
