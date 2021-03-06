from rest_framework.permissions import BasePermission


class UserPermission(BasePermission):

    def has_permission(self, request, view):
        """
        Definimos si un usuario puede usar o no el endpoint
        :param request: HttpRequest
        :param view: UserViewSet
        :return: True si puede, False si no puede
        """

        # cualquiera puede crear un usuario
        if view.action == "create":
            return True

        # cualquiera autenticado puede ver su propio detalle, actualizarlo o borrar su cuenta
        if request.user.is_authenticated() and view.action in ("retrieve", "update", "partial_update", "destroy"):
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