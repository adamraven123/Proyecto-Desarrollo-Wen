from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages


def auth_login(request):
    template_name = 'login.html'
    data = {}

    logout(request)
    username = password = ''

    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            username=username,
            password=password
        )
        if user is not None:
            print("Entre al user is not none")
            if user.is_active:
                print("IS ACTIVE")
                login(request, user)
                print("Pase el login")
                return HttpResponseRedirect(reverse('player_list'))
            else:
                print("usuario o contraseña no validos")
                messages.warning(
                    request,
                    'Usuario o contraseña incorrectos!'
                )
        else:
            print("Usuario incorrecto")
            messages.error(
                request,
                'Usuario o contraseña incorrectos!'
            )
    return render(request, template_name, data)


def auth_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('player_list'))
