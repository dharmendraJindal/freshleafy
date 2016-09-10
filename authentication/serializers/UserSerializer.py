from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = ('id', 'email', 'username','first_name', 'last_name', 'password')
        lookup_field= 'email'
        extra_kwargs = {
            'url': {'lookup_field': 'email'}
        }

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)

        instance.save()

        password = validated_data.get('password', None)

        if password:
            instance.set_password(password)
            instance.save()

            update_session_auth_hash(self.context.get('request'), instance)

        return instance