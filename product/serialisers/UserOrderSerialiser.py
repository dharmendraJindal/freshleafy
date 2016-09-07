from rest_framework import serializers
from product.models import UserOrder
from product.models import OrderedProduct
from product.serialisers.OrderedProductSerialiser import OrderedProductSerialiser


class UserOrderSerialiser(serializers.ModelSerializer):
    ordered_products = serializers.SerializerMethodField()

    class Meta:
        model = UserOrder
        fields = ('order_timestamp', 'ordered_products',)

    def get_ordered_products(self, obj):
        queryset = OrderedProduct.objects.filter(user_order=obj)
        return OrderedProductSerialiser(queryset, many=True).data
