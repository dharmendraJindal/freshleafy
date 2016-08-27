from django.conf.urls import url

from rest_framework_nested import routers
from flapps.authentication.views import AccountViewSet, LoginView, LogoutView

accounts_router = routers.SimpleRouter()
accounts_router.register(r"register", AccountViewSet)

urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
]

urlpatterns += accounts_router.urls
