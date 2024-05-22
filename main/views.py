from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        'title': 'Home - Головна',
        'content': 'Головна сторінка мого сайту - Home',
    }

    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'Home - Про нас',
        'content': 'Про мій сайт - Home',
        'text_on_page': "Мій інтернет-магазин меблів розроблений за допомогою Django"
    }
    return render(request, 'main/about.html', context)