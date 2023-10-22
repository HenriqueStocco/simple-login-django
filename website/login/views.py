from django.shortcuts import render
from django.contrib.auth import login, authenticate
from social_django.utils import psa
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required(login_url='')
def home_page(request):
    return render(request, 'users/home.html')


def login_page(request):
    if request.method == 'GET':
        return render(request, 'users/login.html')

    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return render(request, 'users/home.html')
        else:
            return render(request, 'users/login.html')


def register_page(request):
    if request.method == 'GET':
        return render(request, 'users/register.html')

    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(username=username).first()

        if user:
            return render(request, 'users/register.html')

        user = User.objects.create_user(
            username=username, email=email, password=password)
        user.save()

        return render(request, 'users/login.html')


@psa('social:complete')
def login_by_social(request):
    user = request.user
    if user.is_authenticated:
        return render(request, 'users/home.html')

    if user:
        login(request, user)
        return render(request, 'users/home.html')

    else:
        return render(request, 'users/login.html')
