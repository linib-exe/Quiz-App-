from django.urls import path 
from quizapp import views
urlpatterns = [
    path('get-questions/',views.get_questions,name='get-questions'),
    path('get-quiz/',views.get_quiz,name='get-quiz'),
    path('get-choices/',views.get_choices,name='get-choices'),
    path('create-questions/',views.create_questions,name='create-questions'),
    path('create-quiz/',views.create_quiz,name='create-quiz'),
    path('create-choices/',views.create_choices,name='create-choices'),
    path('update-question/<int:id>',views.update_question,name='update-question'),
    path('update-quiz/<int:id>',views.update_quiz,name='update-quiz'),
    path('update-choice/<int:id>',views.update_choice,name='update-choice'),
    path('delete-question/<int:id>',views.delete_question,name='delete-question'),
]