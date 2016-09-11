from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from product.models import UserOrder
from product.models import Product
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

    def create(self, request, *args, **kwargs):
        ordered_products_data = request.data

        try:
            user_order = UserOrder(user=request.user)
            user_order.save()

            for ordered_product_data in ordered_products_data:
                unit = ordered_product_data.get("unit")
                name = ordered_product_data.get("name")
                rate = ordered_product_data.get("rate")
                quantity = ordered_product_data.get("quantity")

                product = Product.objects.get(name=name)
                ordered_product = OrderedProduct(user_order=user_order, product=product, rate=rate, quantity=quantity,
                                                 unit=unit)
                ordered_product.save()
        except Exception as ex:
            print ex
        return Response({}, status=status.HTTP_200_OK)
