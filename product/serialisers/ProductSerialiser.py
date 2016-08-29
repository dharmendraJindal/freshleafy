from rest_framework import serializers

from product.models import Product
from product.models.RateUnit import RateUnit
from product.serialisers.ProductCategorySerialiser import ProductCategorySerializer


class ProductSerialiser(serializers.ModelSerializer):
    product_category = ProductCategorySerializer(many=True)
    rate = serializers.SerializerMethodField()
    unit = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('name', 'image_path', 'grade','product_category', 'rate', 'unit')

    def get_rate(self, obj):
        try:
            rate_unit = RateUnit.objects.get(product=obj)
            return rate_unit.rate
        except RateUnit.DoesNotExist:
            return

    def get_unit(self, obj):
        try:
            rate_unit = RateUnit.objects.get(product=obj)
            return rate_unit.unit
        except RateUnit.DoesNotExist:
            return
