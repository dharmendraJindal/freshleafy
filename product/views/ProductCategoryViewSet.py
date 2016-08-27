from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from product.models import ProductCategory
from product.serialisers.ProductCategorySerialiser import ProductCategorySerializer


class ProductCategoryViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
