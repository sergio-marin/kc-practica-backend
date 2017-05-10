from django.shortcuts import render

from blogs.models import Post, Blog


def posts_list(request):
    """
    Recupera todos los posts de la bd y los pinta en la página principal
    :param request: HttpRequest
    :return: HttpResponse
    """
    # recuperar todos los posts de la bd
    posts = Post.objects.all()

    # devolver la respuesta
    context = {
        'post_objects': posts
    }

    # renderizar plantilla
    return render(request, 'blogs/latest_posts.html', context)


def blogs_list(request):
    """
    Recupera todos los blogs de la bd y los pinta en la página principal
    :param request: HttpRequest
    :return: HttpResponse
    """
    # recuperar todos los blogs de la bd
    blogs = Blog.objects.all()

    # devolver la respuesta
    context = {
        'blog_objects': blogs
    }

    # renderizar plantilla
    return render(request, 'blogs/blogs_list.html', context)
