from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

from .forms import UserForm
from .models import Film, UserProfile


# Create your views here.


def main(request):
    return render(request, "main.html", {"selected": "main"})


def films(request):
    return render(request, "main.html", {"selected": "films", "items": Film.objects.order_by('-rating')[:5]})


def current_film(request):
    item = Film.get(request.GET.get("id"))
    return render(request, "item.html", {"item": item, "selected": "films"})


def series(request):
    return render(request, "main.html", {"selected": "series"})


def movies(request):
    return render(request, "main.html", {"selected": "movies"})


def authorization(request):
    return render(request, "login.html")


def registration(request):
    form = UserForm(request.POST or None)
    return render(request, "registration.html", {'form':form})


def show_comments(request):
    item = Film.get(request.GET.get("id"))
    return render(request, "item.html", {"comments": [1,2,3], "item": item})


def show_reviews(request):
    item = Film.get(request.GET.get("id"))
    return render(request, "item.html", {"reviews": [1,2,3], "item": item})


def finish_or_repeat_registration(request):
    form_data = UserForm(request.POST or None)
    if form_data.is_valid():
        username = form_data.cleaned_data.get("username")
        password = form_data.cleaned_data.get("password")
        birthday = form_data.cleaned_data.get("birthday")
        about = form_data.cleaned_data.get("about")
        email = form_data.cleaned_data.get("email")
        User.objects.create_user(username=username, password=password)
        user_profile = UserProfile()
        user_profile.username = username
        user_profile.password = password
        user_profile.email = email
        user_profile.about = about
        user_profile.birthday = birthday
        user_profile.save()
        return render(request, "main.html", {"selected": "main"})
    else:
        return render(request, "registration.html", {"form": form_data})


def profile(request):
    profile = UserProfile.get_by_username(request.GET.get("username"))
    return render(request, "main.html", {"selected": "profile", "profile": profile})

