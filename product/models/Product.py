from django.db import models

from product.models import ProductCategory


class Product(models.Model):
    name = models.CharField(max_length=200)
    product_category = models.ManyToManyField(ProductCategory)
    grade = models.CharField(max_length=200)
    image_path = models.CharField(max_length=500, null=True, blank=True)
    rate = models.CharField(max_length=200, default=1)
    unit = models.CharField(max_length=200, default='Kg')
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name