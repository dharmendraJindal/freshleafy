from django.db import models
from product.models import Product
from product.models import UserOrder


class OrderedProduct(models.Model):
    user_order = models.ForeignKey(UserOrder, null=True, blank=True)
    product = models.ForeignKey(Product)
    rate = models.CharField(max_length=200)
    unit = models.CharField(max_length=200)
    quantity = models.CharField(max_length=200)

    def order_timestamp(self):
        return self.user_order.order_timestamp

    def user_email(self):
        return self.user_order.user.email

    def user_name(self):
        return self.user_order.user.first_name + ' '+ self.user_order.user.last_name






