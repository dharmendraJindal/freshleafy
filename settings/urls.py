from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^home/.*$', TemplateView.as_view(template_name='base.html')),
    url(r'^$', TemplateView.as_view(template_name='base.html')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/auth/', include('authentication.urls')),
    url(r'^api/v1/product/', include('product.urls')),
    url(r'^api/v1/files/', include('image.urls')),
]