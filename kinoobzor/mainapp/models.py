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

    def get_count_of_comments(self) -> int:
        count = FilmComment.objects.filter(film_id=self.id).count()
        return count

    def get_count_of_reviews(self):
        count = FilmReview.objects.filter(film_id=self.id).count()
        return count

    def get_comments(self):
        comments = FilmComment.objects.filter(film_id=self.id)
        return comments

    def get_reviews(self):
        reviews = FilmReview.objects.filter(film_id=self.id)
        return reviews

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

    def get_info(self):
        if self.year_end is None:
            year = f"{self.year_start} - Не закончен"
        else:
            year = f"{self.year_start} - {self.year_end}"
        return f"{self.name} ({year})\nРежиссер: {self.director}\n" \
               f"Жанр: {self.genre}\nОценка: {self.rating} "

    def get_count_of_comments(self) -> int:
        count = SeriesComment.objects.filter(series_id=self.id).count()
        return count

    def get_count_of_reviews(self):
        count = SeriesReview.objects.filter(series_id=self.id).count()
        return count

    def get_comments(self):
        comments = SeriesComment.objects.filter(series_id=self.id)
        return comments

    def get_reviews(self):
        reviews = SeriesReview.objects.filter(series_id=self.id)
        return reviews

    def get_years(self):
        if self.year_end is None:
            return f"{self.year_start} - Не закончен"
        else:
            return f"{self.year_start} - {self.year_end}"

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

    def get_info(self):
        return f"{self.name} ({self.year})\nРежиссер: {self.director}\n" \
               f"Жанр: {self.genre}\nОценка: {self.rating} "

    def get_count_of_comments(self) -> int:
        count = MovieComment.objects.filter(movie_id=self.id).count()
        return count

    def get_count_of_reviews(self):
        count = MovieReview.objects.filter(movie_id=self.id).count()
        return count

    def get_comments(self):
        comments = MovieComment.objects.filter(movie_id=self.id)
        return comments

    def get_reviews(self):
        reviews = MovieReview.objects.filter(movie_id=self.id)
        return reviews

    @staticmethod
    def get(movie_id: int) -> 'Movie':
        return Movie.objects.filter(id=movie_id)[0]


class UserProfile(models.Model):
    username = models.CharField(max_length=30, null=False, default='guest')
    password = models.CharField(max_length=30, null=False, default='guest')
    email = models.EmailField(null=False)
    birthday = models.DateField(null=False)
    about = models.TextField(null=False)
    photo = models.ImageField(upload_to='images', blank=True, default='images/default.jpg')
    #{"film":[id1,id2,id3],"series":[id1,id2],"movies":[id1,id2],"comments_film"[id1,id2]
    # "comments_series:[id1,id2], "comments_movies":[id1,id2],"review_film":[id1,id2],
    # "review_series: [id1,id2], "review_movie":[id,id2]
    marks = models.JSONField(blank=True, default=dict())

    @staticmethod
    def get(profile_id: int) -> 'UserProfile':
        return UserProfile.objects.filter(id=profile_id)[0]

    @staticmethod
    def get_by_username(username: str) -> 'UserProfile':
        return UserProfile.objects.filter(username=username)[0]

    def get_subscribers_count(self):
        return UserSubscribers.objects.filter(user_id=self.id).count()

    def get_subscriptions_count(self):
        return UserSubscribers.objects.filter(sub_id=self.id).count()

    def get_subscribers(self):
        return UserSubscribers.objects.filter(user_id=self.id)

    def get_subscriptions(self):
        return UserSubscribers.objects.filter(sub_id=self.id)


class FilmComment(models.Model):
    author_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.TextField(max_length=120)
    date_published = models.DateField(null=False)
    film_id = models.ForeignKey(Film, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    @staticmethod
    def get(id: int):
        return FilmComment.objects.filter(id=id)[0]


class SeriesComment(models.Model):
    author_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.TextField(max_length=120)
    date_published = models.DateField(null=False)
    series_id = models.ForeignKey(Series, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    @staticmethod
    def get(id: int):
        return SeriesComment.objects.filter(id=id)[0]


class MovieComment(models.Model):
    author_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.TextField(max_length=120)
    date_published = models.DateField(null=False)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    @staticmethod
    def get(id: int):
        return MovieComment.objects.filter(id=id)[0]


class FilmReview(models.Model):
    author_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.TextField(max_length=500)
    is_positive = models.BooleanField(null=False)
    date_published = models.DateField(null=False)
    film_id = models.ForeignKey(Film, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    @staticmethod
    def get(id: int):
        return FilmReview.objects.filter(id=id)[0]


class SeriesReview(models.Model):
    author_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.TextField(max_length=500)
    is_positive = models.BooleanField(null=False)
    date_published = models.DateField(null=False)
    series_id = models.ForeignKey(Series, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    @staticmethod
    def get(id: int):
        return SeriesReview.objects.filter(id=id)[0]


class MovieReview(models.Model):
    author_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.TextField(max_length=500)
    is_positive = models.BooleanField(null=False)
    date_published = models.DateField(null=False)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    @staticmethod
    def get(id: int):
        return MovieReview.objects.filter(id=id)[0]

class UserFavoriteFilms(models.Model):
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    film_id = models.ForeignKey(Film, on_delete=models.CASCADE)


class UserFavoriteSeries(models.Model):
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    series_id = models.ForeignKey(Series, on_delete=models.CASCADE)


class UserFavoriteMovies(models.Model):
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)


class NewsForMain(models.Model):
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.TextField(max_length=150)
    date_published = models.DateField(null=False)


class UserSubscribers(models.Model):
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="user")
    sub_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="sub")