from django.conf.urls import url, include
from django.contrib import admin

from flapps.base.BaseView import BaseView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/product/', include('flapps.product.urls', namespace='product'), ),
    url(r'^api/auth/', include('flapps.authentication.urls', namespace='authentication')),
    url(r'^$', BaseView.as_view(), name='base'),
]
