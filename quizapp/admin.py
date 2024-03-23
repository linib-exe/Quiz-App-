from django.contrib import admin
from .models import Question,Quiz,Choice
# Register your models here.
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Choice)