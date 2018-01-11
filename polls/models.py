from django.db import models
from .elastic_search_connection import MoviesearchIndex, BooksearchIndex, ProductsearchIndex #MovieinfoIndex
from django.db.models import signals
from django.utils import timezone

#class Movie_info(models.Model):
#  image_urls = models.CharField(max_length= 200)
#  title = models.CharField(max_length= 100)
#  pub_date = models.CharField(max_length= 200)
#  director =models.CharField(max_length= 100)
#  actor = models.CharField(max_length= 100)
#  userRating = models.CharField(max_length = 10)

#  def indexing(self):
#    movieinfoindex = MovieinfoIndex(
#      meta = {
#        'id':self.id
#      },
#      title = self.title,
#     director = self.director,
#      pub_date = self.pub_date,
#      actor = self.actor,
#      image_urls = self.image_urls,
#      userRating = self.userRating
#    )

 #   movieinfoindex.save()
 #   return movieinfoindex.to_dict(include_meta=True)

class User(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    age = models.IntegerField()
    sex = models.CharField(max_length=5)
    password = models.CharField(max_length=40, default='')
    lastsearch = models.CharField(max_length=40, null = True)

    
    def __str__(self):
        return self.name

class Movie_search(models.Model):

  keyword = models.CharField(max_length = 100, null=True)
  date = models.DateField(default=timezone.now, blank=True)
  age = models.IntegerField(null = True)
  sex = models.CharField(max_length=5, null = True)


  def indexing(self):

    movieinfosearch = MoviesearchIndex(
      meta = {
        'id' : self.id
      },
      keyword = self.keyword,
      date = self.date,
      age = self.age,
      sex = self.sex,
    )

    movieinfosearch.save()

    return movieinfosearch.to_dict(include_meta=True)



class Book_search(models.Model):

  keyword = models.CharField(max_length = 100, null=True)
  date =models.DateField(auto_now=True)
  age = models.IntegerField(null = True)
  sex = models.CharField(max_length=5,  null = True)

  def indexing(self):

    bookinfosearch = BooksearchIndex(
      meta = {
        'id' : self.id
      },
      keyword = self.keyword,
      date = self.date,
      age = self.age,
      sex = self.sex,
    )

    bookinfosearch.save()

    return bookinfosearch.to_dict(include_meta=True)


class Product_search(models.Model):

  keyword = models.CharField(max_length = 100, null=True)
  date =models.DateField(auto_now=True)
  age = models.IntegerField(null = True)
  sex = models.CharField(max_length=5, null = True)

  def indexing(self):

    productinfosearch = ProductsearchIndex(
      meta = {
        'id' : self.id
      },
      keyword = self.keyword,
      date = self.date,
      age = self.age,
      sex = self.sex,
    )

    productinfosearch.save()

    return productinfosearch.to_dict(include_meta=True)

