from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Film(models.Model):
    name = models.CharField(max_length=50)
    director = models.CharField(max_length=50)
    description = models.TextField(null=False)
    year = models.IntegerField(null=False)
    genre = models.CharField(max_length=100)
    rating = models.FloatField(default=0.0)
    poster = models.ImageField(upload_to='images', blank=True)

    def get_info(self) -> str:
        return f"{self.name} ({self.year})\nРежиссер: {self.director}\n" \
               f"Жанр: {self.genre}\nОценка: {self.rating} "

    @staticmethod
    def get(film_id: int) -> 'Film':
        return Film.objects.filter(id=film_id)[0]


class Series(models.Model):
    name = models.CharField(max_length=50)
    director = models.CharField(max_length=50)
    description = models.TextField(null=False)
    year_start = models.IntegerField(null=False)
    year_end = models.IntegerField(blank=True, null=True)
    genre = models.CharField(max_length=100)
    rating = models.FloatField(default=0.0)
    poster = models.ImageField(upload_to='images', blank=True)

    @staticmethod
    def get(series_id: int) -> 'Series':
        return Series.objects.filter(id=series_id)[0]


class Movie(models.Model):
    name = models.CharField(max_length=50)
    director = models.CharField(max_length=50)
    description = models.TextField(null=False)
    year = models.IntegerField(null=False)
    genre = models.CharField(max_length=100)
    rating = models.FloatField(default=0.0)
    poster = models.ImageField(upload_to='images', blank=True)

    @staticmethod
    def get(movie_id: int) -> 'Movie':
        return Movie.objects.filter(id=movie_id)[0]


class UserProfile(models.Model):
    username = models.CharField(max_length=30, null=False, default='guest')
    password = models.CharField(max_length=30, null=False, default='guest')
    email = models.EmailField(null=False)
    birthday = models.DateField(null=False)
    about = models.TextField(null=False)
    photo = models.ImageField(upload_to='images', blank=True)

    @staticmethod
    def get(profile_id: int) -> 'UserProfile':
        return UserProfile.objects.filter(id=profile_id)[0]

    @staticmethod
    def get_by_username(username: str) -> 'UserProfile':
        return UserProfile.objects.filter(username=username)[0]


class FilmComment(models.Model):
    author_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.TextField(max_length=120)
    date_published = models.DateField(null=False)
    film_id = models.ForeignKey(Film, on_delete=models.CASCADE)


class SeriesComment(models.Model):
    author_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.TextField(max_length=120)
    date_published = models.DateField(null=False)
    series_id = models.ForeignKey(Series, on_delete=models.CASCADE)


class MovieComment(models.Model):
    author_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.TextField(max_length=120)
    date_published = models.DateField(null=False)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)


class FilmReview(models.Model):
    author_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.TextField(max_length=500)
    is_positive = models.BooleanField(null=False)
    date_published = models.DateField(null=False)
    film_id = models.ForeignKey(Film, on_delete=models.CASCADE)


class SeriesReview(models.Model):
    author_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.TextField(max_length=500)
    is_positive = models.BooleanField(null=False)
    date_published = models.DateField(null=False)
    series_id = models.ForeignKey(Series, on_delete=models.CASCADE)


class MovieReview(models.Model):
    author_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.TextField(max_length=500)
    is_positive = models.BooleanField(null=False)
    date_published = models.DateField(null=False)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)


class UserFavoriteFilms(models.Model):
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    film_id = models.ForeignKey(Film, on_delete=models.CASCADE)


class UserFavoriteSeries(models.Model):
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    series_id = models.ForeignKey(Series, on_delete=models.CASCADE)


class UserFavoriteMovies(models.Model):
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)