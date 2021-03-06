import ast
import pytz
from datetime import datetime
from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from product.models import OrderedProduct
from product.models import Product
from product.models import UserOrder
from product.serialisers.OrderedProductSerialiser import OrderedProductSerialiser


class UserOrderViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    all_orders = UserOrder.objects.all()
    serializer_class = OrderedProductSerialiser

    def list(self, request, *args, **kwargs):
        user = User.objects.get(username=request.user)
        user_orders = self.all_orders.filter(user=user)
        data = self.get_order_user_order_by(user_orders)
        return Response(data)

    def get_order_user_order_by(self, user_orders):
        orders = []

        for order in user_orders:
            ordered_products = OrderedProduct.objects.filter(user_order=order)

            total_price = 0
            total_quantity = 0
            products = []
            for ordered_product in ordered_products:
                total_price_of_product = 30 * int(ordered_product.quantity)
                total_price += total_price_of_product
                total_quantity += int(ordered_product.quantity)
                product_data = {
                    "rate": ordered_product.rate,
                    "quantity_intervals": {
                        "pack_size_types": ["100 gm", "200 gm", "500 gm", "1 Kg", "5 Kg"],
                        "pack_size_rates": [30, 60, 100, 150, 200]
                    },
                    "quantity": ordered_product.quantity,
                    "image_path": ordered_product.product.image_path,
                    "unit": ordered_product.unit,
                    "name": ordered_product.product.name,
                    "hindi_name": ordered_product.product.name,
                }
                products.append(product_data)

            order_datetime = self.convert_to_local_timezone(order.order_timestamp)

            order_dict = {
                "total_price": total_price,
                "total_quantity": total_quantity,
                "date_time": order_datetime.strftime("%b %d %H:%M %p"),
                "products": products
            }
            orders.append(order_dict)
        return orders

    def convert_to_local_timezone(self, date_time):
        return date_time.replace(tzinfo=pytz.utc).astimezone(pytz.timezone("Asia/Kolkata"))

    def create(self, request, *args, **kwargs):
        request_data = request.data

        # ordered_products_data = request_data.get("data")
        ordered_products_data = request.data

        try:
            user_order = UserOrder(user=request.user)
            user_order.save()
            self.create_post_order_data(user_order, ordered_products_data)


        except Exception as ex:
            print ex
        return Response(request.data)

    def create_post_order_data(self, user_order, ordered_products_data):
        for product in ordered_products_data:
            product_obj = Product.objects.get(id=int(product.get("product_id")))

            unit = product_obj.unit
            rate = product_obj.rate
            quantity = product.get("quantity")
            ordered_product = OrderedProduct(user_order=user_order, product=product_obj, rate=rate, quantity=quantity,
                                             unit=unit)
            ordered_product.save()
            print "Order successfully saved"
        return
