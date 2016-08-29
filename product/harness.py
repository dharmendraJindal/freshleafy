import django
django.setup()

from product.models import Product
from product.models import ProductCategory
from product.models import RateUnit


def add_test_product():
    # p1 = Product(name='Potato', grade="A", image_path="/static/product_images/potato.jpeg")
    # p1.save()
    #
    # RU1= RateUnit(product=p1, rate=30, unit="Kg")
    # RU1.save()
    #
    # p2 = Product(name='Tomato', grade="A", image_path="/static/product_images/tomato.jpeg")
    # p2.save()
    #
    # RU2 = RateUnit(product=p2, rate=80, unit="Kg")
    # RU2.save()

    p3 = Product(name='Apple', grade="A", image_path="/static/product_images/apple.jpeg")
    p3.save()

    RU3 = RateUnit(product=p3, rate=80, unit="Kg")
    RU3.save()

def add_pc_to_p():
    # vpc = ProductCategory.objects.get(name = 'Vegetables')
    #
    # p = Product.objects.get(name='Tomato')
    # p.product_category.add(vpc)
    # p.save()
    # print p.product_category.all()

    fpc = ProductCategory.objects.get(name='Fruits')

    p = Product.objects.get(name='Apple')
    p.product_category.add(fpc)
    p.save()
    print p.product_category.all()


# add_test_product()

add_pc_to_p()
