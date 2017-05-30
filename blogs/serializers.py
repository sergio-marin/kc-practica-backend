from rest_framework import serializers

from blogs.models import Blog, Post


class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = ("id",)


class BlogListSerializer(BlogSerializer):
    url = serializers.CharField(source='get_absolute_url', read_only=True)

    class Meta(BlogSerializer.Meta):
        fields = ("name", "url")


class PostSerializer(serializers.ModelSerializer):
    blog = BlogSerializer(read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('blog',)


class PostsListSerializer(PostSerializer):

    class Meta(PostSerializer.Meta):
        fields = ("title", "media_url", "introduction", "published_date")
