from django.contrib.auth.models import User
from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet

from users.serializers import UserSerializer


class UserViewSet(CreateModelMixin, GenericViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
