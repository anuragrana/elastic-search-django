from django.contrib import admin
from .models import Question

# Register your models here.

# Need to register Question so it shows up in the admin
admin.site.register(Question)