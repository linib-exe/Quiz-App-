from django.urls import path 
from quizapp import views
urlpatterns = [
    path('get-questions/',views.get_questions,name='get-questions'),
    path('get-quiz/',views.get_quiz,name='get-quiz'),
    path('get-choices/',views.get_choices,name='get-choices'),
    path('create-questions/',views.create_questions,name='create-questions'),
]