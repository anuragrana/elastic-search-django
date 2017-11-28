from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import DocType, Text, Date

# creates a global connection to elastic search
connections.create_connection()


# defines what needs to index in elastic search
class QuestionsIndex(DocType):
    author = Text()
    question_text = Text()
    pub_date = Date()

    class Meta:
        # name of index. Will be used in search
        index = 'questions-index'