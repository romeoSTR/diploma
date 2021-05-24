from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

from .forms import UserForm, CommentaryForm, ReviewForm
from .models import Film, UserProfile, FilmComment, MovieComment, SeriesComment, FilmReview, SeriesReview, MovieReview, \
    Series, Movie
import datetime


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
    comments = item.get_comments()
    if len(comments) == 0:
        comments = "Нет комментариев"
    return render(request, "item.html", {"comments": comments, "item": item, "selected": item_type})


def show_reviews(request):
    item_type = request.GET.get("item")
    if item_type == "film":
        item = Film.get(request.GET.get("id"))
    elif item_type == "series":
        item = Series.get(request.GET.get("id"))
    else:
        item = Movie.get(request.GET.get("id"))
    reviews = item.get_reviews()
    if len(reviews) == 0:
        reviews = "Нет рецензий"
    return render(request, "item.html", {"reviews": reviews, "item": item, "selected": item_type})


def finish_or_repeat_registration(request):
    form_data = UserForm(request.POST or None)
    if form_data.is_valid():
        username = form_data.cleaned_data.get("username")
        password = form_data.cleaned_data.get("password")
        birthday = form_data.cleaned_data.get("birthday")
        about = form_data.cleaned_data.get("about")
        email = form_data.cleaned_data.get("email")
        photo = form_data.cleaned_data.get("photo")
        User.objects.create_user(username=username, password=password)
        user_profile = UserProfile()
        user_profile.username = username
        user_profile.password = password
        user_profile.email = email
        user_profile.about = about
        user_profile.birthday = birthday
        if photo:
            user_profile.photo = photo
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
    comments = item.get_comments()
    form_data = CommentaryForm()
    return render(request, "item.html", {"comments": comments, "form": form_data, "selected":item_type, "item": item, "add_comment": 1})


def add_review(request):
    item_type = request.GET.get("item")
    if item_type == "film":
        item = Film.get(request.GET.get("id"))
    elif item_type == "series":
        item = Series.get(request.GET.get("id"))
    else:
        item = Movie.get(request.GET.get("id"))
    reviews = item.get_reviews()
    form_data = ReviewForm()
    return render(request, "item.html", {"reviews": reviews, "form": form_data, "selected": item_type, "item": item, "add_review": 1})


def delete_comment(request):
    item_type = request.GET.get("item")
    if item_type == "film":
        comment = FilmComment.get(request.GET.get("comment"))
        item = Film.get(request.GET.get("id"))
    elif item_type == "series":
        comment = SeriesComment.get(request.GET.get("comment"))
        item = Series.get(request.GET.get("id"))
    else:
        comment = MovieComment.get(request.GET.get("comment"))
        item = Movie.get(request.GET.get("id"))
    comment.delete()
    comments = item.get_comments()
    if len(comments) == 0:
        comments = "Нет комментариев"
    return render(request, "item.html", {"comments": comments, "item": item, "selected": item_type})


def delete_review(request):
    item_type = request.GET.get("item")
    if item_type == "film":
        review = FilmReview.get(request.GET.get("review"))
        item = Film.get(request.GET.get("id"))
    elif item_type == "series":
        review = SeriesReview.get(request.GET.get("review"))
        item = Series.get(request.GET.get("id"))
    else:
        review = MovieReview.get(request.GET.get("review"))
        item = Movie.get(request.GET.get("id"))
    review.delete()
    reviews = item.get_reviews()
    if len(reviews) == 0:
        reviews = "Нет рецензий"
    return render(request, "item.html", {"reviews": reviews, "item": item, "selected": item_type})


def save_comment(request):
    item_type = request.GET.get("item")
    user = UserProfile.get_by_username(request.GET.get("user"))
    form_data = CommentaryForm(request.POST or None)
    is_valid = True
    if form_data.is_valid():
        text = form_data.cleaned_data.get("text")
    else:
        is_valid = False
    if item_type == "film":
        item = Film.get(request.GET.get("id"))
        if is_valid:
            comment = FilmComment()
            comment.film_id = item
    elif item_type == "series":
        item = Series.get(request.GET.get("id"))
        if is_valid:
            comment = SeriesComment()
            comment.series_id = item
    else:
        item = Movie.get(request.GET.get("id"))
        if is_valid:
            comment = MovieComment()
            comment.movie_id = item
    if is_valid:
        comment.text = text
        comment.author_id = user
        comment.date_published = datetime.date.today()
        comment.save()
        comments = item.get_comments()
        return render(request, "item.html",
                      {"comments": comments, "selected": item_type, "item": item})
    else:
        comments = item.get_comments()
        return render(request, "item.html",
                      {"comments": comments, "form": form_data, "selected": item_type, "item": item, "add_comment": 1})


def save_review(request):
    item_type = request.GET.get("item")
    user = UserProfile.get_by_username(request.GET.get("user"))
    form_data = ReviewForm(request.POST or None)
    is_valid = True
    if form_data.is_valid():
        text = form_data.cleaned_data.get("text")
        is_positive = form_data.cleaned_data.get("is_positive")
    else:
        is_valid = False
    if item_type == "film":
        item = Film.get(request.GET.get("id"))
        if is_valid:
            review = FilmReview()
            review.film_id = item
    elif item_type == "series":
        item = Series.get(request.GET.get("id"))
        if is_valid:
            review = SeriesReview()
            review.series_id = item
    else:
        item = Movie.get(request.GET.get("id"))
        if is_valid:
            review = MovieReview()
            review.movie_id = item
    if is_valid:
        review.text = text
        review.author_id = user
        review.is_positive = is_positive
        review.date_published = datetime.date.today()
        review.save()
        reviews = item.get_reviews()
        return render(request, "item.html",
                      {"reviews": reviews, "selected": item_type, "item": item})
    else:
        reviews = item.get_reviews()
        return render(request, "item.html",
                      {"reviews": reviews, "form": form_data, "selected": item_type, "item": item, "add_review": 1})

