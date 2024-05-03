from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories


def index(request):

    categories = Categories.objects.all()


    context = {
        'title': 'SNEAKER - Головна',
        'content': 'Головна сторінка мого сайту - SNEAKER',
        'categories': categories
    }

    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'Home - Про нас',
        'content': 'Про мій сайт - SNEAKER',
        'text_on_page': "Мій сайт такий крутий, ну дуже крутий"
    }
    return render(request, 'main/about.html', context)