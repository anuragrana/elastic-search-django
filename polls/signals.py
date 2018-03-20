from .models import Movie_search, Book_search, Product_search #Movie_info,
from django.db.models.signals import post_save
from django.dispatch import receiver

#@receiver(post_save, sender= Movie_info)
#def index_movie_info(sender, instance, created,**kwargs):
#	instance.indexing()

# 데이터 베이스 저장 될 때에 저장된 데이터가 엘라스틱 서치로 날라가게 하는 트리거 설정(데이터 저장시 각 모델의 indexing() 함수 발동) 


@receiver(post_save, sender= Movie_search)
def index_movie_info(sender, instance, created,**kwargs):
	instance.indexing()

@receiver(post_save, sender = Book_search)
def index_search_info(sender, instance, created, **kwargs):
	instance.indexing()

@receiver(post_save, sender = Product_search)
def index_product_info(sender, instance, created, **kwargs):
	instance.indexing()