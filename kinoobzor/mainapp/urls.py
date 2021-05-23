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
    url(r'add_comment', views.add_comment, name='add_comment'),
    url(r'add_review', views.add_review, name='add_review'),
    url(r'save_comment', views.save_comment, name='save_comment'),
    url(r'save_review', views.save_review, name='save_review'),
    url(r'^film/', views.current_film, name='current_film'),
    url(r'^movie/', views.current_movie, name='current_movie'),
    url(r'^series/', views.current_series, name='current_series'),
    url(r'finish', views.finish_or_repeat_registration, name="finish_or_repeat_registration"),
    url(r'profile', views.profile, name="profile"),
]