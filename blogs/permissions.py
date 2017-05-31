from rest_framework.permissions import BasePermission


class PostsPermissions(BasePermission):

    def has_permission(self, request, view):
        """
        Definimos si un usuario puede usar o no el endpoint
        :param request: HttpRequest
        :param view: UserViewSet
        :return: True si puede, False si no puede
        """

        # cualquiera puede listar o ver el detalle de un post publicado
        if view.action in ("retrieve", "list"):
            return True

        # cualquiera autenticado puede crear, acceder al detalle, actualizar o borrar sus propios posts
        if request.user.is_authenticated() and view.action in ("create", "update", "partial_update", "destroy"):
            return True

        return False

    def has_object_permission(self, request, view, obj):
        """
        Permite acceso si la accion es 'retrieve' o si el usuario es el admin o el propio blogger
        :param request: HttpRequest
        :param view: UserViewSet
        :param obj: User
        :return: True si puede, False si no puede
        """
        return view.action == 'retrieve' or request.user.is_superuser or request.user == obj.blog.blogger