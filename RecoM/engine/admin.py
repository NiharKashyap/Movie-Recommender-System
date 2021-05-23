from django.contrib import admin
from .models import Movies, Ratings

# Register your models here.


class MoviesAdmin(admin.ModelAdmin):
    list_display=('movie_title', 'movie_poster')

class RatingsAdmin(admin.ModelAdmin):
    list_display=('user_id', 'movie_id', 'rating')


admin.site.register(Movies, MoviesAdmin)
admin.site.register(Ratings, RatingsAdmin)