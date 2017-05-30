from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

from blogs.models import Blog
from blogs.serializers import BlogListSerializer


class BlogViewSet(ListModelMixin, GenericViewSet):

    queryset = Blog.objects.all()
    serializer_class = BlogListSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = "blogger__username"
    ordering_fields = "name"

