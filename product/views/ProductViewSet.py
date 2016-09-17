from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from product.models import Product
from product.models import ProductCategory
from product.serialisers.ProductSerialiser import ProductSerialiser


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerialiser

    def list(self, request, *args, **kwargs):
        product_category_name = request.GET.get('product_category_name', None)
        if product_category_name:
            try:
                product_category = ProductCategory.objects.get(name=product_category_name)
                self.queryset = Product.objects.filter(product_category=product_category)
            except ProductCategory.DoesNotExist:
                print "Product Category Not Found, Sending All Products"
                pass
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)
