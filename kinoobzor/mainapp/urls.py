from django.conf.urls import url
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
    url(r'^film/', views.current_film, name='current_film'),
    url(r'^comments', views.show_comments, name='show_comments')
]