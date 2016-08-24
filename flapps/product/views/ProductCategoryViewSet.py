
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from flapps.product.models import ProductCategory
from flapps.product.serialisers.ProductCategorySerialiser import ProductCategorySerializer


class ProductCategoryViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = ProductCategory.objects.all()
    print queryset
    serializer_class = ProductCategorySerializer
