from django.conf.urls import url

from flapps.base.views.ProductView import product_view

urlpatterns = [
    url(r'^app/', product_view, name='app'),
    url(r'^$', product_view, name='app'),
]
