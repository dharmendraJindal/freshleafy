from django.conf.urls import url, include
from django.contrib import admin

import authentication
from authentication.urls import accounts_router
from base.IndexView import IndexView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='base'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/auth/', include(authentication.urls)),
    url(r'^api/v1/product/', include('product.urls')),
]

# urlpatterns += router.urls
