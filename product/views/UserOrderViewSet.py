from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from product.models import UserOrder
from product.models import OrderedProduct
from product.serialisers.OrderedProductSerialiser import OrderedProductSerialiser


class UserOrderViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    all_orders = UserOrder.objects.all()
    serializer_class = OrderedProductSerialiser

    def list(self, request, *args, **kwargs):
        user = request.user
        user_orders = self.all_orders.filter(user=user)
        queryset = OrderedProduct.objects.filter(user_order__in=user_orders)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)