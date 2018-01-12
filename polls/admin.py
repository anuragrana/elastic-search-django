from django.contrib import admin
from .models import Movie_search, Book_search, Product_search, User #Movie_info

# Register your models here.

#admin.site.register(Movie_info)
admin.site.register(Movie_search)
admin.site.register(Product_search)
admin.site.register(Book_search)
admin.site.register(User)
