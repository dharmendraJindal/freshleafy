from django.conf.urls import url, include
from django.contrib import admin

from base.IndexView import IndexView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='base'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/auth/', include('authentication.urls')),
    url(r'^api/v1/product/', include('product.urls')),
    url(r'^api/v1/files/', include('image.urls')),
]

# urlpatterns += router.urls
