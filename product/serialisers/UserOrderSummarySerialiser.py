from rest_framework import serializers
from product.models.UserOrderSummary import UserOrderSummary
from product.serialisers.OrderedProductSerialiser import OrderedProductSerialiser


class UserOrderSummarySerialiser(serializers.ModelSerializer):
    ordered_product = OrderedProductSerialiser(many=True)

    class Meta:
        model = UserOrderSummary
        fields = ('order_timestamp', 'ordered_product',)
