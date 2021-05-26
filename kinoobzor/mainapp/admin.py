from django.contrib import admin
from .models import Film, Series, Movie, UserProfile, FilmComment, UserSubscribers, NewsForMain

# Register your models here.
admin.site.register(Film)
admin.site.register(Series)
admin.site.register(Movie)
admin.site.register(UserProfile)
admin.site.register(FilmComment)
admin.site.register(UserSubscribers)
admin.site.register(NewsForMain)