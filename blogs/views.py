from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views import View

from blogs.forms import NewPostForm
from blogs.models import Post, Blog


def posts_list(request):
    """
    Recupera todos los posts publicados de BD y los pinta en la página principal
    :param request: HttpRequest
    :return: HttpResponse
    """
    # recuperar todos los posts de la bd
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

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

    posts = Post.objects.filter(blog=blog.pk).filter(published_date__lte=timezone.now()).order_by('-published_date')

    # preparar el contexto
    context = {
            'blog_object': blog,
            'post_objects': posts
        }

    # renderizar plantilla
    return render(request, 'blogs/blog_detail.html', context)


def post_detail(request, blogger_name, post_pk):
    """
    Recupera un post de BD y lo pinta
    :param request: HttpRequest
    :param post_pk: La pk del post a visualizar
    :return: HttpResponse
    """
    # recuperar el post
    try:
        post = Post.objects.get(pk=post_pk)
    except Post.DoesNotExist:
        return render(request, '404.html', {}, status=404)

    # preparar el contexto
    context = {
            'post_object': post
        }

    # renderizar plantilla
    return render(request, 'blogs/post_detail.html', context)


class NewPostView(View):
    @method_decorator(login_required)
    def get(self, request):
        # crear el formulario
        form = NewPostForm()

        # renderiza la plantilla con el formulario
        context = {
            "form": form
        }
        return render(request, 'blogs/new_post.html', context)

    @method_decorator(login_required)
    def post(self, request):
        """
        Formulario para publicar post, se debe estar validado
        :param request: HttpRequest
        :return: HttpResponse
        """
        # crear el formulario con los datos del POST
        blog = Blog.objects.filter(blogger=request.user).get()
        post_with_blog = Post(blog=blog)
        form = NewPostForm(request.POST, instance=post_with_blog)

        # validar el formulario
        if form.is_valid():
            # crear la tarea
            post = form.save()

            # mostrar mensaje de éxito
            message = 'Your post has been published! <a href="{0}">View Post</a>'.format(
                reverse('post_detail', args=[request.user.username, post.pk])  # genera la URL de detalle de este post
            )

            # limpiamos el formulario creando uno nuevo vacío para pasar a la plantilla
            form = NewPostForm()
        else:
            # mostrar mensaje de error
            message = "An error ocurred!"

        # renderizar la plantilla
        context = {
            "form": form,
            "message": message
        }
        return render(request, 'blogs/new_post.html', context)
