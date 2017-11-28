from .models import Question
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=Question)
def index_question(sender, instance, **kwargs):
    instance.indexing()