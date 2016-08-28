from django.conf.urls import url

from rest_framework import routers
from authentication.views import AccountViewSet, LoginView, LogoutView

router = routers.DefaultRouter()
router.register(r'register', AccountViewSet)

#test done git

urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
]

urlpatterns += router.urls


