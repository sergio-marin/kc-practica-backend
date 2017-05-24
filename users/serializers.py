from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def validate(self, attrs):  # no es necesario validar si el username esta vacio o ya existe, se hace por defecto
        attrs["first_name"] = attrs.get('first_name', '').lower().capitalize()
        attrs["last_name"] = attrs.get('last_name', '').lower().capitalize()
        attrs["email"] = attrs.get('email', '').lower()
        attrs["username"] = attrs.get('username', '').lower()

        return attrs