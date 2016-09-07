from django.contrib.auth.models import User
from django.db import models

from product.models.OrderedProduct import OrderedProduct



class UserOrderSummary(models.Model):
    user = models.ForeignKey(User)
    ordered_product = models.ManyToManyField(OrderedProduct)
    order_timestamp = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.user.username
