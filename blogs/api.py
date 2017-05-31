from django.db.models import Q
from django.utils import timezone
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from blogs.models import Blog, Post
from blogs.permissions import PostsPermissions
from blogs.serializers import BlogListSerializer, PostsListSerializer, PostSerializer


class BlogViewSet(ListModelMixin, GenericViewSet):

    queryset = Blog.objects.all()
    serializer_class = BlogListSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ("blogger__username",)
    ordering_fields = ("name",)


class PostViewSet(ModelViewSet):

    queryset = Post.objects.select_related('blog__blogger').all().order_by('-published_date')
    serializer_class = PostSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ("title", "body", "introduction")
    ordering_fields = ("title", "published_date")
    permission_classes = (IsAuthenticatedOrReadOnly, PostsPermissions)

    def get_serializer_class(self):
        """
        Devolvemos un serializador distinto cuando la acción es list
        """
        return self.serializer_class if self.action != 'list' else PostsListSerializer

    def get_queryset(self):
        """
        Definimos los posts a devolver según el tipo de usuario que los solicita
        """
        # si no esta autenticado sólo devolvemos los posts publicados
        if not self.request.user.is_authenticated():
            return self.queryset.filter(published_date__lte=timezone.now())
        # si es admin devolvemos todos los posts
        elif self.request.user.is_superuser:
            return self.queryset
        # finalmente devolvemos todos los posts del blogger en particular
        else:
            return self.queryset.filter(blog=self.request.user.blog)

    def perform_create(self, serializer):
        serializer.save(blog=self.request.user.blog)
        return serializer