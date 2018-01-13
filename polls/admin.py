from django.contrib import admin
from .models import Movie_search, Book_search, Product_search, User #Movie_info

# 데이터 베이스 정보(모델명)를 관리자 사이트에서 관리할 수 있도록 하는 코드 

#admin.site.register(Movie_info)
admin.site.register(Movie_search)
admin.site.register(Product_search)
admin.site.register(Book_search)
admin.site.register(User)
