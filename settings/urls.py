from django.conf.urls import url, include
from django.contrib import admin

from base.views.IndexView import IndexView
from base.views.HomeView import HomeView

urlpatterns = [
    # url(r'^$', HomeView.as_view(), name='home'),
    url(r'^$', IndexView.as_view(), name='base'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/auth/', include('authentication.urls')),
    url(r'^api/v1/product/', include('product.urls')),
    url(r'^api/v1/files/', include('image.urls')),
]

#handling page not found

handler404='base.views.CustomErrorView.handle_page_not_found_404'