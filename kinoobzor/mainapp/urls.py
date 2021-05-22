from django.conf.urls import url
from django.urls import path, include

from . import views


app_name = 'mainapp'

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^main$', views.main, name='main'),
    url(r'^filmss$', views.films, name='films'),
    url(r'^seriess$', views.series, name='series'),
    url(r'^movies$', views.movies, name='movies'),
    url(r'^authorization$', views.authorization, name='authorization'),
    url(r'^registration$', views.registration, name='registration'),
    url(r'comments', views.show_comments, name='show_comments'),
    url(r'reviews', views.show_reviews, name='show_reviews'),
    url(r'^film/', views.current_film, name='current_film'),
    url(r'finish', views.finish_or_repeat_registration, name="finish_or_repeat_registration"),
    url(r'profile', views.profile, name="profile"),
]