from django.shortcuts import render


def registration(request):
    context = {
        'title': 'SNEAKER - Реєстрація',
    }

    return render(request, 'users/registration.html', context)


def profile(request):
    context = {
        'title': 'SNEAKER - Профіль',
    }
    return render(request, 'users/profile.html', context)


def login(request):
    context = {
        'title': 'SNEAKER - Увійти',
    }
    return render(request, 'users/login.html', context)


def logout(request):
    ...