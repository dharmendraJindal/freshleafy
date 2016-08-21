from rest_framework import serializers, viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

# Serializers define the API representation.
from freshleafy.flapps.product.models import ProductCategory


class ProductCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ('name',)


# ViewSets define the view behavior.
class ProductCategoryViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
