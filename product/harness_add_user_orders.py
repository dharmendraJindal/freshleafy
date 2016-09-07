import django
django.setup()

from product.models.OrderedProduct import OrderedProduct
from product.models.UserOrderSummary import UserOrderSummary
from product.models.Product import Product
from product.models.RateUnit import RateUnit
from django.contrib.auth.models import User

def add_sample_user_orders():

    product = Product.objects.get(name='Tomato')
    p_rateunit = RateUnit.objects.get(product=product)
    user = User.objects.get(username='webadmin')
    print user
    print p_rateunit

    op, created = OrderedProduct.objects.get_or_create(product=product, rate=p_rateunit.rate, unit=p_rateunit.unit, quantity=10)


    uos, created = UserOrderSummary.objects.get_or_create(user=user)
    uos.save()
    uos.ordered_product.add(op)
    uos.save()

    uos.save()

def print_user_orders():
    user = User.objects.get(username='webadmin')

    uos = UserOrderSummary.objects.filter(user=user)
    print uos


# add_sample_user_orders()
print_user_orders()