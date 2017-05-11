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
from django.conf.urls import url
from django.contrib import admin
from blogs.views import posts_list, blogs_list, blog_detail, post_detail

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # Posts URLs
    url(r'^$', posts_list),
    url(r'^blogs/?$', blogs_list),
    url(r'^blogs/(?P<blogger_name>[a-zA-Z0-9_]+)/?$', blog_detail),
    url(r'^blogs/(?P<blogger_name>[a-zA-Z0-9_]+)/(?P<post_pk>[0-9]+)/?$', post_detail),
]
