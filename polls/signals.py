from .models import Movie_search, Book_search, Product_search #Movie_info,
from django.db.models.signals import post_save
from django.dispatch import receiver

#@receiver(post_save, sender= Movie_info)
#def index_movie_info(sender, instance, created,**kwargs):
#	instance.indexing()



@receiver(post_save, sender= Movie_search)
def index_movie_info(sender, instance, created,**kwargs):
	instance.indexing()

@receiver(post_save, sender = Book_search)
def index_search_info(sender, instance, created, **kwargs):
	instance.indexing()

@receiver(post_save, sender = Product_search)
def index_product_info(sender, instance, created, **kwargs):
	instance.indexing()