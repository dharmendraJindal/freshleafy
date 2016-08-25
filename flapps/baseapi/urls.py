from django.conf.urls import url, include

urlpatterns = [
    url(r'^product/', include('flapps.product.urls', namespace='product')),
]
