from rest_framework_nested import routers
from image.views import AddEditPicturesView

pictures_router = routers.SimpleRouter()
pictures_router.register(r"image", AddEditPicturesView)
urlpatterns = pictures_router.urls
