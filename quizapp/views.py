from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Question, Choice, Quiz
from rest_framework.response import Response
from .serializers import QuestionSerializer, QuizSerializer, ChoiceSerializer
from rest_framework.decorators import api_view
from rest_framework import status

def home(request):
    questions = Question.objects.all()
    if request.method == 'POST':
        score = 0
        total_questions = Question.objects.count()
        for question in questions:
            selected_choice_id = request.POST.get(f'question{question.id}')
            print(selected_choice_id)
            correct_choice = Choice.objects.get(question=question, is_correct=True)
            if int(selected_choice_id) == correct_choice.id:
                score += 1
        messages.success(request, f'You scored {score} out of {total_questions}')
        return redirect('home')
    return render(request, 'home.html', {'questions': questions})


#-----------rest-framework-----------------------------------------------------------
@api_view(['GET'])
def get_questions(request):
    questions = Question.objects.all()
    serializer = QuestionSerializer(questions,many=True)
    return Response(
        {
            'data':serializer.data,
            'status':status.HTTP_200_OK
        }
    )

@api_view(['GET'])
def get_quiz(request):
    quizs = Quiz.objects.all()
    serializer = QuizSerializer(quizs,many=True)
    return Response(
        {
            'data':serializer.data,
            'status':status.HTTP_200_OK
        }
    )

@api_view(['GET'])
def get_choices(request):
    choices = Choice.objects.all()
    serializer = ChoiceSerializer(choices,many=True)
    return Response(
        {
            'data':serializer.data,
            'status':status.HTTP_200_OK
        }
    )

@api_view(['POST'])
def create_questions(request):
    data = request.data
    serializer = QuestionSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {
                'status':status.HTTP_200_OK,
                'data':serializer.data
            }
        )
    else:
        return Response(
            {
                'message':"Bad request"
            }
        )

