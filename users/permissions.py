from rest_framework.permissions import BasePermission


class UserPermission(BasePermission):

    def has_permission(self, request, view):
        """
        Define si un usuario puede usar o no un endpoint
        :param request: HttpRequest
        :param view: UserViewSet
        :return: True si puede, False si no puede
        """

        # cualquiera puede crear un usuario
        if view.action == "create":
            return True

        # cualquiera autenticado puede acceder al detalle para ver, actualizar o borrar
        if request.user.is_authenticated() and view.action in ("retrieve", "update", "partial_update"):
            return True

        return False

    def has_object_permission(self, request, view, obj):
        """
        Define si un usuario puede realizar la acción sobre un objeto concreto
        :param request: HttpRequest
        :param view: UserViewSet
        :param obj: User
        :return: True si puede, False si no puede
        """
        # sólo si es admin o es el propio usuario
        return request.user.is_superuser or request.user == obj