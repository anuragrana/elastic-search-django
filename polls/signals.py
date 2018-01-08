from .models import Question, Movie_info
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=Question)
def index_question(sender, instance, **kwargs):
    instance.indexing()

@receiver(post_save, sender=Movie_info)
def index_movie_info(sender, instance, **kwargs):
	instance.indexing()