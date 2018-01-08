from django.db import models
from .elastic_search_connection import QuestionsIndex, MovieinfoIndex


class Question(models.Model):
    author = models.CharField(max_length=100)
    question_text = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('date published')


    # indexing method of Question model
    def indexing(self):
       obj = QuestionsIndex(
            meta = {
                'id':self.id
            },
            author = self.author,
            pub_date = self.pub_date,
            question_text = self.question_text
       )
       obj.save()
       return obj.to_dict(include_meta=True)


class Movie_info(models.Model):
  image_urls = models.CharField(max_length= 200)
  title = models.CharField(max_length= 100)
  pub_date = models.IntegerField()
  director =models.CharField(max_length= 100)
  actor = models.CharField(max_length= 100)
  userRating = models.CharField(max_length = 10)

  def indexing(self):
    obj = MovieinfoIndex(
      meta = {
        'id':self.id
      },
      title = self.title,
      pub_date = self.pub_date,
      director = self.director,
      actor = self.actor,
      image_urls = self.image_urls,
      userRating = self.userRating
      )

    obj.save()
    return obj.to_dict(include_meta=True)