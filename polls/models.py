from django.db import models
from .elastic_search_connection import MoviesearchIndex, BooksearchIndex #MovieinfoIndex
from django.db.models import signals



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



class Movie_search(models.Model):

  keyword = models.CharField(max_length = 100)


  def indexing(self):

    movieinfosearch = MoviesearchIndex(
      meta = {
        'id' : self.id
      },
      keyword = self.keyword
    )

    movieinfosearch.save()

    return movieinfosearch.to_dict(include_meta=True)



class Book_search(models.Model):

  keyword = models.CharField(max_length = 100)


  def indexing(self):

    bookinfosearch = BooksearchIndex(
      meta = {
        'id' : self.id
      },
      keyword = self.keyword
    )

    bookinfosearch.save()

    return bookinfosearch.to_dict(include_meta=True)

