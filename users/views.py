from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from .forms import UserLoginForm, UserRegistrationForm, UserProfileForm, ProfileForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:login'))
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
        if user:
            auth.login(request, user)
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
