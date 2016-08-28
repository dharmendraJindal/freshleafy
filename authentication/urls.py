from django.conf.urls import url

from rest_framework import routers
from authentication.views.AccountViewSet import AccountViewSet
from authentication.views.LoginView import LoginView
from authentication.views.LogoutView import LogoutView

router = routers.DefaultRouter()
router.register(r'register', AccountViewSet, base_name="register")

#test done

urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
]

urlpatterns += router.urls


