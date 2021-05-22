from django.contrib import admin
from .models import Film, Series, Movie, UserProfile

# Register your models here.
admin.site.register(Film)
admin.site.register(Series)
admin.site.register(Movie)
admin.site.register(UserProfile)