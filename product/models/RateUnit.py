from django.db import models

from product.models import Product


class RateUnit(models.Model):
    product = models.ForeignKey(Product)
    rate = models.CharField(max_length=200)
    unit = models.CharField(max_length=200)

    def __unicode__(self):
        return "%s per %s" % (self.rate, self.unit)