from django.db import models

from image.models import Picture
from product.models import ProductCategory


class Product(models.Model):
    name = models.CharField(max_length=200)
    product_category = models.ManyToManyField(ProductCategory)
    grade = models.CharField(max_length=200)
    image = models.OneToOneField(Picture, null=True, blank=True)

    def __unicode__(self):
        return self.name
