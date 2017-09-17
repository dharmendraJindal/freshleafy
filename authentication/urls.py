from django.conf.urls import url, include
from rest_framework.authtoken import views

from rest_framework import routers
from authentication.views.AccountViewSet import AccountViewSet
from authentication.views.LoginView import LoginView
from authentication.views.LogoutView import LogoutView
from authentication.views.CheckUserExistView import CheckUserExistView

router = routers.DefaultRouter(trailing_slash=True)
router.register(r'register', AccountViewSet, base_name="register")

#test done git

urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^checkuserexist/$', CheckUserExistView.as_view(), name='check_user_exist'),
    url(r'^oauth2/', include("oauth2_provider.urls", namespace="oauth2_provider")),
]

urlpatterns += router.urls

