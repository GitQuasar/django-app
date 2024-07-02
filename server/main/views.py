from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

# def index(request) -> HttpResponse:
#     return HttpResponse('Home Page')


def index(request) -> HttpResponse:
    context = {
        "title": "Home Page",
        "content": "Welcome to the Home Page",
    }

    return render(request, "main/index.html", context)


def about(request) -> HttpResponse:
    return HttpResponse("About Page")
