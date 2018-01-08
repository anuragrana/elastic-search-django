from django.contrib import admin
from .models import Question, Movie_info

# Register your models here.

# Need to register Question so it shows up in the admin
admin.site.register(Question)
admin.site.register(Movie_info)