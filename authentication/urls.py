from django.conf.urls import url

from rest_framework import routers
from authentication.views.AccountViewSet import AccountViewSet
from authentication.views.LoginView import LoginView
from authentication.views.LogoutView import LogoutView
from authentication.views.CheckUserExistView import CheckUserExistView

router = routers.DefaultRouter()
router.register(r'register', AccountViewSet, base_name="register")

#test done git

urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^checkuserexist/$', CheckUserExistView.as_view(), name='check_user_exist'),
]

urlpatterns += router.urls


