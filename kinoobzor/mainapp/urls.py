from django.conf.urls import url
from django.urls import path, include

from . import views


app_name = 'mainapp'

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^main$', views.main, name='main'),
    url(r'^filmss', views.films, name='films'),
    url(r'^seriess', views.series, name='series'),
    url(r'^movies', views.movies, name='movies'),
    url(r'^authorization$', views.authorization, name='authorization'),
    url(r'^registration$', views.registration, name='registration'),
    url(r'profile_comments', views.show_profile_comments, name='show_profile_comments'),
    url(r'profile_reviews', views.show_profile_reviews, name='show_profile_reviews'),
    url(r'like_comment', views.like_comment, name='like_comments'),
    url(r'like_review', views.like_review, name='like_review'),
    url(r'dislike_comment', views.like_comment, name='dislike_comment'),
    url(r'dislike_review', views.like_review, name='dislike_review'),
    url(r'comments', views.show_comments, name='show_comments'),
    url(r'reviews', views.show_reviews, name='show_reviews'),
    url(r'add_comment', views.add_comment, name='add_comment'),
    url(r'add_review', views.add_review, name='add_review'),
    url(r'delete_comment', views.delete_comment, name='delete_comment'),
    url(r'delete_review', views.delete_review, name='delete_review'),
    url(r'save_comment', views.save_comment, name='save_comment'),
    url(r'save_review', views.save_review, name='save_review'),
    url(r'^film/', views.current_film, name='current_film'),
    url(r'^movie/', views.current_movie, name='current_movie'),
    url(r'^series/', views.current_series, name='current_series'),
    url(r'finish', views.finish_or_repeat_registration, name="finish_or_repeat_registration"),
    url(r'save_edit_profile', views.save_edit_profile, name='save_edit_profile'),
    url(r'profile', views.profile, name="profile"),
    url(r'add_to_favorites', views.add_to_favorites, name='add_to_favorites'),
    url(r'del_from_favorites', views.delete_from_favorites, name='delete_from_favorites'),
    url(r'favorites', views.show_favorites, name='show_favorites'),
    url(r'subscribers', views.show_subscribers, name='show_subscribers'),
    url(r'subscriptions', views.show_subscriptions, name='show_subscriptions'),
    url(r'edit', views.edit_profile, name='edit_profile'),
    url(r'subscribe', views.sub_on_profile, name='sub_on_profile'),
    url(r'delete_sub', views.delete_sub_on_profile, name='delete_sub_on_profile'),
    url(r'set_mark', views.set_mark, name='set_mark'),
]