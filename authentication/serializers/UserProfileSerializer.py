from rest_framework import serializers

from authentication.models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    user_id = serializers.SerializerMethodField()
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile

    def get_username(self, obj):
        user = obj.user
        return user.username

    def get_user_id(self, obj):
        user = obj.user
        return user.id

    def get_first_name(self, obj):
        user = obj.user
        return user.first_name

    def get_last_name(self, obj):
        user = obj.user
        return user.last_name

    def get_email(self, obj):
        user = obj.user
        return user.email
