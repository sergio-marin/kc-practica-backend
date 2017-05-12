from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View

from users.forms import LoginForm, SignupForm


class LoginView(View):

    def get(self, request):
        """
        Muestra el formulario de login
        :param request:  HttpRequest
        :return: HttpResponse
        """
        context = {
            'form': LoginForm()
        }
        return render(request, 'users/login.html', context)

    def post(self, request):
        """
        Hace login de un usuario
        :param request:  HttpRequest
        :return: HttpResponse
        """
        form = LoginForm(request.POST)
        context = dict()
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                # usuario autenticado
                django_login(request, user)
                url = request.GET.get('next', 'posts_list')
                return redirect(url)
            else:
                # usuario no autenticado
                context["error"] = "Wrong username or password."
        context["form"] = form
        return render(request, 'users/login.html', context)


def logout(request):
    """
    Hace logout de un usuario
    :param request:  HttpRequest
    :return: HttpResponse
    """
    django_logout(request)
    return redirect('login')


class SignupView(View):

    def get(self, request):
        """
        Muestra el formulario de registro
        :param request:  HttpRequest
        :return: HttpResponse
        """
        context = {
            'form': SignupForm()
        }
        return render(request, 'users/signup.html', context)

    def post(self, request):
        """
        Crea el nuevo usuario en BD
        :param request:  HttpRequest
        :return: HttpResponse
        """
        # crear el formulario con los datos del POST
        form = SignupForm(request.POST)

        # validar el formulario
        if form.is_valid():
            # crear el usuario
            form.save()

            # enviar a página de bienvenida
            return render(request, 'users/signup_succes.html')
        else:
            # mostrar mensaje de error
            message = "An error ocurred! Please try again later."

            # renderizar la plantilla
            context = {
                "form": form,
                "message": message
            }
            return render(request, 'users/signup.html', context)
