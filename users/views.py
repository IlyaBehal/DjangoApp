from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from users.forms import UserLoginForm, UserRegisterForm



def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            print(user)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()

    context = {
        'title': 'SNEAKER - Увійти',
        'form': form
    }
    return render(request, 'users/login.html', context)


def registration(request):
    
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegisterForm()

    context = {
        'title': 'SNEAKER - Реєстрація',
        'form': form

    }

    return render(request, 'users/registration.html', context)


def profile(request):
    context = {
        'title': 'SNEAKER - Профіль',
    }
    return render(request, 'users/profile.html', context)





def logout(request):
    auth.logout(request)
    return redirect(reverse('main:index'))