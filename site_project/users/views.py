from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import User
import json

from .forms import RegisterForm, LoginForm


def signup_user(request):
    if request.user.is_authenticated:
        return redirect(to='quotes_list:main')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotes_list:main')
        else:
            return render(request, 'users/signup.html', context={"form": form})

    return render(request, 'users/signup.html', context={"form": RegisterForm()})


def login_user(request):
    if request.user.is_authenticated:
        return redirect(to='quotes_list:main')

    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is None:
            messages.error(request, 'Username or password didn\'t match')
            return redirect(to='users:login')

        login(request, user)
        return redirect(to='quotes_list:main')

    return render(request, 'users/login.html', context={"form": LoginForm()})

@login_required
def log_out_user(request):
    logout(request)
    return redirect(to='quotes_list:main')


@login_required
def profile(request):
    return render(request, 'users/profile.html')

@login_required
def script(request):
    with open("script/user_list.json") as fh:
        user_list = json.load(fh)

    for us in user_list:
        User.objects.get_or_create(first_name=us["nickname"], email=us["email"], username=us["login"])

    return redirect(to='quotes_list:main')