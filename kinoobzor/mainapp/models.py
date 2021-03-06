import math

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
    marks_count = models.IntegerField(default=1)
    marks = models.IntegerField(default=0)
    poster = models.ImageField(upload_to='images', blank=True)

    def get_info(self) -> str:
        return f"{self.name} ({self.year})\nРежиссер: {self.director}\n" \
               f"Жанр: {self.genre}\nОценка: {float('{:.1f}'.format(self.rating))} "

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

    @staticmethod
    def get_pages():
        films = Film.objects.count()
        pages = films / 5
        return math.ceil(pages)

    def get_marked_users(self):
        users = UserProfile.objects.all()
        usernames = []
        for user in users:
            if self.id in user.marks["film"]:
                usernames.append(user.username)
        return usernames


class Series(models.Model):
    name = models.CharField(max_length=50)
    director = models.CharField(max_length=50)
    description = models.TextField(null=False)
    year_start = models.IntegerField(null=False)
    year_end = models.IntegerField(blank=True, null=True)
    genre = models.CharField(max_length=100)
    rating = models.FloatField(default=0.0)
    poster = models.ImageField(upload_to='images', blank=True)
    marks_count = models.IntegerField(default=1)
    marks = models.IntegerField(default=0)

    @staticmethod
    def get_pages():
        series = Series.objects.count()
        pages = series / 5
        return math.ceil(pages)

    def get_info(self):
        if self.year_end is None:
            year = f"{self.year_start} - Не закончен"
        else:
            year = f"{self.year_start} - {self.year_end}"
        return f"{self.name} ({year})\nРежиссер: {self.director}\n" \
               f"Жанр: {self.genre}\nОценка: {float('{:.1f}'.format(self.rating))} "

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

    def get_marked_users(self):
        users = UserProfile.objects.all()
        usernames = []
        for user in users:
            if self.id in user.marks["series"]:
                usernames.append(user.username)
        return usernames

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
    marks = models.IntegerField(default=0)
    marks_count = models.IntegerField(default=1)

    @staticmethod
    def get_pages():
        movies = Movie.objects.count()
        pages = movies / 5
        return math.ceil(pages)


    def get_info(self):
        return f"{self.name} ({self.year})\nРежиссер: {self.director}\n" \
               f"Жанр: {self.genre}\nОценка: {float('{:.1f}'.format(self.rating))}"

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

    def get_marked_users(self):
        users = UserProfile.objects.all()
        usernames = []
        for user in users:
            if self.id in user.marks["movies"]:
                usernames.append(user.username)
        return usernames

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
    marks = models.JSONField(blank=True, default={"film":[], "series":[], "movies":[],
                                                  "comment_film":[], "comment_series":[], "comment_movies":[],
                                                  "review_film":[], "review_series":[], "review_movie":[]})

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

    def get_favorite_films(self):
        return UserFavoriteFilms.objects.filter(user_id=self.id)

    def get_favorite_series(self):
        return UserFavoriteSeries.objects.filter(user_id=self.id)

    def get_favorite_movies(self):
        return UserFavoriteMovies.objects.filter(user_id=self.id)

    def get_favorite_films_ids(self):
        films = UserFavoriteFilms.objects.filter(user_id=self.id)
        ids = []
        for item in films:
            ids.append(item.film_id.id)
        return ids

    def get_favorite_series_ids(self):
        series = UserFavoriteSeries.objects.filter(user_id=self.id)
        ids = []
        for item in series:
            ids.append(item.series_id.id)
        return ids

    def get_favorite_movies_ids(self):
        movies = UserFavoriteMovies.objects.filter(user_id=self.id)
        ids = []
        for item in movies:
            ids.append(item.movie_id.id)
        return ids

    @staticmethod
    def delete_favorite_film(film_id: int, user_id: int):
        item = UserFavoriteFilms.get(user_id, film_id)
        item.delete()

    @staticmethod
    def delete_favorite_series(series_id: int, user_id: int):
        item = UserFavoriteSeries.get(user_id, series_id)
        item.delete()

    @staticmethod
    def delete_favorite_movie(movie_id: int, user_id: int):
        item = UserFavoriteMovies.get(user_id, movie_id)
        item.delete()

    def get_count_of_comments(self):
        films = FilmComment.objects.filter(author_id=self.id).count()
        series = SeriesComment.objects.filter(author_id=self.id).count()
        movies = MovieComment.objects.filter(author_id=self.id).count()
        return films+series+movies

    def get_count_of_reviews(self):
        films = FilmReview.objects.filter(author_id=self.id).count()
        series = SeriesReview.objects.filter(author_id=self.id).count()
        movies = MovieReview.objects.filter(author_id=self.id).count()
        return films+series+movies

    def get_subs_usernames(self):
        subs = self.get_subscribers()
        names = []
        for sub in subs:
            names.append(sub.sub_id.username)
        return names

    def get_all_user_comments(self):
        films = FilmComment.objects.filter(author_id=self.id)
        series = SeriesComment.objects.filter(author_id=self.id)
        movies = MovieComment.objects.filter(author_id=self.id)
        comments = []
        for item in films:
            comments.append(item)
        for item in series:
            comments.append(item)
        for item in movies:
            comments.append(item)
        return comments

    def get_all_user_reviews(self):
        films = FilmReview.objects.filter(author_id=self.id)
        series = SeriesReview.objects.filter(author_id=self.id)
        movies = MovieReview.objects.filter(author_id=self.id)
        reviews = []
        for item in films:
            reviews.append(item)
        for item in series:
            reviews.append(item)
        for item in movies:
            reviews.append(item)
        return reviews

    @staticmethod
    def get_users():
        return UserProfile.objects.all()


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

    def get_marked_usernames(self):
        users = UserProfile.objects.all()
        usernames = []
        for user in users:
            if self.id in user.marks["comment_film"]:
                usernames.append(user.username)
        return usernames


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

    def get_marked_usernames(self):
        users = UserProfile.objects.all()
        usernames = []
        for user in users:
            if self.id in user.marks["comment_series"]:
                usernames.append(user.username)
        return usernames


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

    def get_marked_usernames(self):
        users = UserProfile.objects.all()
        usernames = []
        for user in users:
            if self.id in user.marks["comment_movie"]:
                usernames.append(user.username)
        return usernames


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

    def get_marked_usernames(self):
        users = UserProfile.objects.all()
        usernames = []
        for user in users:
            if self.id in user.marks["review_film"]:
                usernames.append(user.username)
        return usernames


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

    def get_marked_usernames(self):
        users = UserProfile.objects.all()
        usernames = []
        for user in users:
            if self.id in user.marks["review_series"]:
                usernames.append(user.username)
        return usernames


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

    def get_marked_usernames(self):
        users = UserProfile.objects.all()
        usernames = []
        for user in users:
            if self.id in user.marks["review_movie"]:
                usernames.append(user.username)
        return usernames

class UserFavoriteFilms(models.Model):
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    film_id = models.ForeignKey(Film, on_delete=models.CASCADE)

    @staticmethod
    def get(user_id: int, film_id: int):
        return UserFavoriteFilms.objects.filter(user_id=user_id, film_id=film_id)


class UserFavoriteSeries(models.Model):
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    series_id = models.ForeignKey(Series, on_delete=models.CASCADE)

    @staticmethod
    def get(user_id: int, series_id: int):
        return UserFavoriteSeries.objects.filter(user_id=user_id, series_id=series_id)


class UserFavoriteMovies(models.Model):
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)

    @staticmethod
    def get(user_id: int, movie_id: int):
        return UserFavoriteMovies.objects.filter(user_id=user_id, movie_id=movie_id)


class NewsForMain(models.Model):
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.TextField(max_length=150)
    date_published = models.DateField(null=False)

    @staticmethod
    def get_user_news(user_id: int):
        return NewsForMain.objects.filter(user_id=user_id).order_by('-date_published')


class UserSubscribers(models.Model):
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="user")
    sub_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="sub")

    @staticmethod
    def get_by_sub_and_user_id(user_id: int, sub_id: int):
        return UserSubscribers.objects.filter(user_id=user_id, sub_id=sub_id)[0]

    @staticmethod
    def get_user_subs(user_id: int):
        return UserSubscribers.objects.filter(user_id=user_id)

    @staticmethod
    def get_user_subscriptions(sub_id: int):
        return UserSubscribers.objects.filter(sub_id=sub_id)