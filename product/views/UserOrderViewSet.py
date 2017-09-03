from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from django.contrib.auth.models import User
from product.models import UserOrder
from product.models import Product
from product.models import OrderedProduct
from product.serialisers.OrderedProductSerialiser import OrderedProductSerialiser


class UserOrderViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticatedOrReadOnly,)
    all_orders = UserOrder.objects.all()
    serializer_class = OrderedProductSerialiser

    def list(self, request, *args, **kwargs):
        # user = request.user
        user = User.objects.get(username="webadmin")
        user_orders = self.all_orders.filter(user=user)
        data = self.get_order_user_order_by(user_orders)

        # OrderedProduct.objects.all().delete()
        # UserOrder.objects.all().delete()
        # queryset = OrderedProduct.objects.filter(user_order__in=user_orders)
        # serializer = self.serializer_class(queryset, many=True)
        # return Response(serializer.data)
        # return Response(self.dummy_data())
        return Response(data)

    def get_order_user_order_by(self, user_orders):
        orders = []

        for order in user_orders:
            ordered_products = OrderedProduct.objects.filter(user_order=user_orders)

            total_price = 0
            total_quantity = 0
            for ordered_product in ordered_products:
                total_price += int(ordered_product.rate)
                total_quantity += int(ordered_product.quantity)

            order_dict = {
                "total_price": total_price,
                "total_quantity": total_quantity,
                "date_time": order.order_timestamp.strftime("%b %d %H:%M:%S"),
            }
            orders.append(order_dict)
        return orders

    def create(self, request, *args, **kwargs):
        ordered_products_data = request.data

        try:
            print ordered_products_data, "======="
            user_order = UserOrder(user=User.objects.get(username="webadmin"))
            user_order.save()
            self.create_post_order_data(user_order)


        except Exception as ex:
            print ex
        return Response({}, status=status.HTTP_200_OK)

    def create_post_order_data(self, user_order):
        ordered_products_data = Product.objects.all()[:3]
        for product in ordered_products_data:
            unit = product.unit
            name = product.name
            rate = product.rate
            quantity = 10

            product = Product.objects.get(name=name)
            ordered_product = OrderedProduct(user_order=user_order, product=product, rate=rate, quantity=quantity,
                                             unit=unit)
            ordered_product.save()
            print "Order succseefully saved"
        return

    def dummy_data(self):
        return [
            {
                "date_time": "Sunday 3 sep 17, 4 AM",
                "total_quantity": 3,
                "total_price": 1072,
            },
            {
                "date_time": "Sunday 5 sep 17, 01 PM",
                "total_quantity": 3,
                "total_price": 1072,
            },
            {
                "date_time": "Sunday 9 sep 17, 09:30 PM",
                "total_quantity": 3,
                "total_price": 1072,
            }
        ]
