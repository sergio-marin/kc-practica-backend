from rest_framework.permissions import BasePermission


class PostsPermissions(BasePermission):



    def has_object_permission(self, request, view, obj):
        """
        Permite acceso si la accion es 'retrieve' o si el usuario es el admin o el propio blogger
        :param request: HttpRequest
        :param view: UserViewSet
        :param obj: User
        :return: True si puede, False si no puede
        """
        return view.action == 'retrieve' or request.user.is_superuser or request.user == obj.blog.blogger