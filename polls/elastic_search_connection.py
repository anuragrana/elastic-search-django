from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import DocType, Text, Date

# creates a global connection to elastic search
connections.create_connection()


class MovieinfoIndex(DocType):
    title = Text()
    director = Text()
    pub_date = Text()
    actor = Text()
    image_urls = Text()
    userRating = Text()

    class Meta:
        # name of index. Will be used in search
        index = 'movieinfo-index'

# defines what needs to index in elastic search
class QuestionsIndex(DocType):
    author = Text()
    question_text = Text()
    pub_date = Date()

    class Meta:
        # name of index. Will be used in search
        index = 'questions-index'


