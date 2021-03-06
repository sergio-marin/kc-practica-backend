"""PracticaBackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from blogs.api import BlogViewSet, PostViewSet
from blogs.views import posts_list, blogs_list, blog_detail, post_detail, NewPostView
from users.api import UserViewSet
from users.views import LoginView, logout, SignupView

router = DefaultRouter()
router.register("users", UserViewSet, base_name="users_api")
router.register("blogs", BlogViewSet)
router.register("posts", PostViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # Posts URLs
    url(r'^$', posts_list, name="posts_list"),
    url(r'^blogs/?$', blogs_list, name="blogs_list"),
    url(r'^blogs/(?P<blogger_name>[a-zA-Z0-9_]+)/?$', blog_detail, name="blog_detail"),
    url(r'^blogs/(?P<blogger_name>[a-zA-Z0-9_]+)/(?P<post_pk>[0-9]+)/?$', post_detail, name="post_detail"),
    url(r'^new-post/?$', NewPostView.as_view(), name="new_post"),

    # Users URLs
    url(r'^login$', LoginView.as_view(), name="login"),
    url(r'^logout$', logout, name="logout"),
    url(r'^signup/?$', SignupView.as_view(), name="signup"),

    # APIs URLs
    url(r'^api/1.0/', include(router.urls)),
]
