from django.db import models
from product.models import Product


class OrderedProduct(models.Model):
    product = models.ForeignKey(Product)
    rate = models.CharField(max_length=200)
    unit = models.CharField(max_length=200)
    quantity = models.CharField(max_length=200)




