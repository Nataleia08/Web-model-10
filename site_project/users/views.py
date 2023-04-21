from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect

from .model_users import RegisterForm


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