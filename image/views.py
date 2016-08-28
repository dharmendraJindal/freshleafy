from rest_framework.viewsets import ModelViewSet
from image.serializers import PictureUploadSerializer
from .models import Picture


class AddEditPicturesView(ModelViewSet):
    queryset = Picture.objects.all().order_by('-id')
    serializer_class = PictureUploadSerializer
