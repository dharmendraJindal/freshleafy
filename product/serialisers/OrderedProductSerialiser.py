
from rest_framework import serializers
from product.models.OrderedProduct import OrderedProduct


class OrderedProductSerialiser(serializers.ModelSerializer):
    product_name = serializers.SerializerMethodField()
    order_timestamp = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()

    class Meta:
        model = OrderedProduct
        fields = ('product_name', 'rate', 'unit', 'quantity', 'price', 'order_timestamp')

    def get_product_name(self, obj):
        return obj.product.name

    def get_price(self, obj):
        return float(obj.quantity) * float(obj.rate)

    def get_order_timestamp(self, obj):
        return obj.user_order.order_timestamp