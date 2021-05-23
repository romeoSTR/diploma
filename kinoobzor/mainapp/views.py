from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

from .forms import UserForm, CommentaryForm, ReviewForm
from .models import Film, UserProfile, FilmComment, MovieComment, SeriesComment, FilmReview, SeriesReview, MovieReview, \
    Series, Movie


# Create your views here.


def main(request):
    return render(request, "main.html", {"selected": "main"})


def films(request):
    return render(request, "main.html", {"selected": "film", "items": Film.objects.order_by('-rating')})


def series(request):
    return render(request, "main.html", {"selected": "series", "items": Series.objects.order_by('-rating')})


def movies(request):
    return render(request, "main.html", {"selected": "movie", "items": Movie.objects.order_by('-rating')})


def current_film(request):
    item = Film.get(request.GET.get("id"))
    return render(request, "item.html", {"item": item, "selected": "film"})


def current_series(request):
    item = Series.get(request.GET.get("id"))
    return render(request, "item.html", {"item": item, "selected": "series"})


def current_movie(request):
    item = Movie.get(request.GET.get("id"))
    return render(request, "item.html", {"item": item, "selected": "movie"})


def authorization(request):
    return render(request, "login.html")


def registration(request):
    form = UserForm(request.POST or None)
    return render(request, "registration.html", {'form':form})


def show_comments(request):
    item_type = request.GET.get("item")
    if item_type == "film":
        item = Film.get(request.GET.get("id"))
    elif item_type == "series":
        item = Series.get(request.GET.get("id"))
    else:
        item = Movie.get(request.GET.get("id"))
    return render(request, "item.html", {"comments": [1,2,3], "item": item, "selected": item_type})


def show_reviews(request):
    item_type = request.GET.get("item")
    if item_type == "film":
        item = Film.get(request.GET.get("id"))
    elif item_type == "series":
        item = Series.get(request.GET.get("id"))
    else:
        item = Movie.get(request.GET.get("id"))
    return render(request, "item.html", {"reviews": [1,2,3], "item": item, "selected": item_type})


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


def add_comment(request):
    item_type = request.GET.get("item")
    if item_type == "film":
        item = Film.get(request.GET.get("id"))
    elif item_type == "series":
        item = Series.get(request.GET.get("id"))
    else:
        item = Movie.get(request.GET.get("id"))
    form_data = CommentaryForm()
    return render(request, "item.html", {"comments": [1,2,3], "form": form_data, "selected":item_type, "item": item, "add_comment": 1})


def add_review(request):
    print(1)
    item_type = request.GET.get("item")
    if item_type == "film":
        item = Film.get(request.GET.get("id"))
    elif item_type == "series":
        item = Series.get(request.GET.get("id"))
    else:
        item = Movie.get(request.GET.get("id"))
    form_data = ReviewForm()
    return render(request, "item.html", {"reviews": [1,2,3], "form": form_data, "selected": item_type, "item": item, "add_review": 1})


def save_comment(request):
    return


def save_review(request):
    return

