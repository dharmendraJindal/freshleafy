from rest_framework import serializers

from authentication.models import UserProfile
from authentication.serializers.UserSerializer import UserSerializer


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer
    class Meta:
        model = UserProfile