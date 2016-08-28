from rest_framework import serializers
from rest_framework.fields import FileField
from image.models import Picture


class PictureUploadSerializer(serializers.HyperlinkedModelSerializer):
    file = FileField(allow_empty_file=False, required=True)

    class Meta:
        model = Picture
        fields = ("slug", "file", "name", "thumbnail", "id")
