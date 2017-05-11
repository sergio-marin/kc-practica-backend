from django.http import HttpResponse
from django.shortcuts import render

from blogs.models import Post, Blog


def posts_list(request):
    """
    Recupera todos los posts de BD y los pinta en la página principal
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
    Recupera todos los blogs de BD y los pinta en la página principal
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


def blog_detail(request, blogger_name):
    """
    Recupera un blog de BD y pinta sus posts (primero los más recientes)
    :param request: HttpRequest
    :param blogger: El usuario del blog a recuperar
    :return: HttpResponse
    """
    # recuperar el blog
    try:
        blog = Blog.objects.filter(blogger__username=blogger_name).get()
    except Blog.DoesNotExist:
        return render(request, '404.html', {}, status=404)
    except Blog.MultipleObjectsReturned:
        return HttpResponse("More than one blog owned by the user.", status=300)

    posts = Post.objects.filter(blog=blog.pk).order_by('-published_date')

    # preparar el contexto
    context = {
            'blog_object': blog,
            'post_objects': posts
        }

    # renderizar plantilla
    return render(request, 'blogs/blog_detail.html', context)
