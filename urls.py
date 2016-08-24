from django.conf.urls import url, include
from django.contrib import admin

import view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', view.test, name='index'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include('flapps.apibase.urls', namespace='apibase')),
]
