from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import DocType, Text, Date, Integer

# creates a global connection to elastic search
connections.create_connection()


#class MovieinfoIndex(DocType):
#    title = Text()
#    director = Text()
#    pub_date = Text()
#    actor = Text()
#    image_urls = Text()
#    userRating = Text()

#    class Meta:
        # name of index. Will be used in search
 #       index = 'movieinfo-index'


class MoviesearchIndex(DocType): # 검색된 영화 키워드 데이터 엘라스틱 서치 모델 필드
	keyword = Text()
	date = Date()
	age = Integer()
	sex = Text()

	class Meta:
		index = 'moviesearch-index'  # 엘라스틱 서치로 넘어 갈떄 인덱스 이름


class BooksearchIndex(DocType):  # 검색된 책 키워드 데이터 엘라스틱 서치 모델 필드
	keyword = Text()
	date = Date()
	age = Integer()
	sex = Text()

	class Meta:
		index = 'booksearch-index' # 엘라스틱 서치로 넘어 갈떄 인덱스 이름


class ProductsearchIndex(DocType):  # 검색된 제품 키워드 데이터 엘라스틱 서치 모델 필드
	keyword = Text()
	date = Date()
	age = Integer()
	sex = Text()

	class Meta:
		index = 'productsearch-index' # 엘라스틱 서치로 넘어 갈떄 인덱스 이름