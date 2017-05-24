from django.contrib.auth.models import User
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from users.permissions import UserPermission
from users.serializers import UserSerializer


class UserViewSet(CreateModelMixin, RetrieveModelMixin, GenericViewSet):

    permission_classes = (UserPermission,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


