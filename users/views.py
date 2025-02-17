from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect

from carts.models import Cart
from .forms import UserLoginForm, UserRegistrationForm, UserProfileForm, ProfileForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()

            session_key = request.session.session_key  # Получаем сессионный ключ анонимного юзера

            user = form.instance
            auth.login(request, user)
            if session_key:
                Cart.objects.filter(session_key=session_key).update(user=user)  # Добавление  корзину анонима к рег. юзеру
            return HttpResponseRedirect(reverse('main:index'))

    else:
        form = UserRegistrationForm()
    context = {'form': form}

    return render(request, 'users/register.html', context=context)


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        session_key = request.session.session_key  # Получаем сессионный ключ анонимного юзера

        if user:
            auth.login(request, user)
            Cart.objects.filter(session_key=session_key).update(
                user=user)  # Добавляем корзину анонима к авторизованному юзеру
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()

    context = {'form': form}
    return render(request, 'users/login.html', context=context)


@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = ProfileForm(instance=request.user)
    context = {'form': form}
    return render(request, 'users/profile.html', context=context)


def users_cart(request):
    return render(request, 'users/users_cart.html')


@login_required
def logout(request):
    auth.logout(request)
    return redirect(reverse('main:index'))
