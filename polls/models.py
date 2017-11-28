from django.db import models
from .elastic_search_connection import QuestionsIndex


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