from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request) -> HttpResponse:
    context = {
        "title": "Home Comfort - Главная",
        "content": "Магазин мебели Home Comfort",
    }

    return render(request, "main/index.html", context)


def about(request) -> HttpResponse:
    context = {
        "title": "Home Comfort - О нас",
        "content": "О нас",
        "text_on_page": "Здесь мы говорим, почему этот магазин такой классный, а также о том, какой хороший у нас товар",
    }

    return render(request, "main/about.html", context)
