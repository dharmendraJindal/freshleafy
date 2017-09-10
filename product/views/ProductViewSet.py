#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from product.models import Product
from product.models import ProductCategory
from product.serialisers.ProductSerialiser import ProductSerialiser


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
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

    def dummy_data(self):
        data = {
            "name":"some_name",
            "pass":"some_pass",
            "email":"some_email",
        }
        return [
            {
                "name": "Dhaniya",
                "hindi_name": "धनिया",
                "image_path": "/static/product_images/coriander_dhania.jpg",
                "quantity_types": [
                    1,5, 10,50,100
                ],
                "rate": "50",
                "unit": "Kg",
                "product_id": 1
            },
            {
                "name": "Guava",
                "hindi_name": "अमरुद",
                "image_path": "/static/product_images/guava_peru_500_gm.jpg",
                "quantity_types": [
                    1,5, 10,50,100
                ],
                "rate": "80",
                "unit": "Kg",
                "product_id": 2
            },
            {
                "name": "Tomato",
                "hindi_name": "टमाटर",
                "image_path": "/static/product_images/cherry_tomato_250_gm.jpg",
                "quantity_types": [
                    1,5, 10,50,100
                ],
                "rate": "150",
                "unit": "Kg",
                "product_id": 3
            },
            {
                "name": "Kakdi",
                "hindi_name": "ककड़ी",
                "image_path": "/static/product_images/cucumber_kakdi_500.jpg",
                "grade": "A",
                "quantity_types": [
                    1,5, 10,50,100
                ],
                "rate": "30",
                "unit": "Kg",
                "product_id": 4
            },
            {
                "name": "Mango",
                "hindi_name": "आम",
                "image_path": "/static/product_images/mango_totapuri.jpg",
                "grade": "A",
                "quantity_types": [
                    1,5, 10,50,100
                ],
                "rate": "250",
                "unit": "Kg",
                "product_id": 4
            }
        ]
