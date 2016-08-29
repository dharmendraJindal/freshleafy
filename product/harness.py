import django
django.setup()

from product.models import Product
from product.models import RateUnit


def add_test_product():
    p1 = Product(name='Potato', grade="A", image_path="/static/product_images/potato.jpeg")
    p1.save()

    RU1= RateUnit(product=p1, rate=30, unit="Kg")
    RU1.save()

    p2 = Product(name='Tomato', grade="A", image_path="/static/product_images/tomato.jpeg")
    p2.save()

    RU2 = RateUnit(product=p2, rate=80, unit="Kg")
    RU2.save()


add_test_product()
