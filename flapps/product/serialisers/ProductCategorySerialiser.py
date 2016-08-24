from rest_framework import serializers

from flapps.product.models import ProductCategory


class ProductCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ('name',)