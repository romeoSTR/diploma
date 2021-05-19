from django.contrib import admin
from .models import Film, Series, Movie

# Register your models here.
admin.site.register(Film)
admin.site.register(Series)
admin.site.register(Movie)