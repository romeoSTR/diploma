from django.http import HttpResponse
from django.shortcuts import render
from .models import Film

# Create your views here.


def main(request):
    return render(request, "main.html", {"selected": "main"})


def films(request):
    return render(request, "main.html", {"selected": "films", "items": Film.objects.order_by('-rating')[:5]})


def current_film(request):
    item = Film.get(request.GET.get("id"))
    return render(request, "item.html", {"item": item})


def series(request):
    return render(request, "main.html", {"selected": "series"})


def movies(request):
    return render(request, "main.html", {"selected": "movies"})


def authorization(request):
    return render(request, "authorization.html")


def registration(request):
    return render(request, "registration.html")


def show_comments(request):
    item = Film.get(request.GET.get("id"))
    return render(request, "item.html", {"comments": True, "item": item})