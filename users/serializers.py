from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        return self.update(User(), validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        if validated_data.get('password'):
            instance.set_password(validated_data.get('password'))
        instance.save()
        return instance