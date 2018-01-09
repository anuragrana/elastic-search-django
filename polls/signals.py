from .models import Movie_info, Movie_search
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender= Movie_info)
def index_movie_info(sender, instance, created,**kwargs):
	instance.indexing()



@receiver(post_save, sender= Movie_search)
def index_movie_info(sender, instance, created,**kwargs):
	instance.indexing()
