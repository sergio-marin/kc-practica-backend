from django.contrib.auth.models import User
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet

from users.permissions import UserPermission
from users.serializers import UserSerializer


class UserViewSet(CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericViewSet):

    permission_classes = (UserPermission,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

