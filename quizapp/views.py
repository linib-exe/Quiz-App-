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
#-------------------------CREATE-----------------------------------------------------
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

@api_view(['POST'])   
def create_quiz(request):
    data = request.data
    serializer = QuizSerializer(data=data)
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
                'message':"Bad Request"
            }
        )

@api_view(['POST'])    
def create_choices(request):
    data = request.data
    serializer = ChoiceSerializer(data=data)
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
                'message':'Bad Request'
            }
        )

#----------------------------------READ-------------------------------------------------
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

#----------------------------UPDATE--------------------------------------------------------
@api_view(['PUT','PATCH'])
def update_question(request,id):
    question  = Question.objects.get(id =id)
    serializer = QuestionSerializer(question,data=request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {
                'data':serializer.data,
                'status':status.HTTP_200_OK,
                'message':'Data Updated Successfully'
            }
        )
    else:
        return Response(
            {
                'message':'Error updating question',
                'status':status.HTTP_400_BAD_REQUEST,
                'errors':serializer.errors
            }
        )

@api_view(['PUT','PATCH'])
def update_quiz(request,id):
    quiz = Quiz.objects.get(id=id)
    data = request.data
    serializer = QuizSerializer(quiz,data=data,partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {
                'message':'Data Updated Successfully',
                'data':serializer.data,
                'status':status.HTTP_200_OK
            }
        )
    else:
        return Response(
            {
                'message':'Error updating quiz',
                'status':status.HTTP_400_BAD_REQUEST,
            }
        )

@api_view(['PUT','PATCH'])
def update_choice(request,id):
    choice = Choice.objects.get(id=id)
    data = request.data
    serializer = QuizSerializer(choice,data=data,partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {
                'message':'Data Updated Successfully',
                'data':serializer.data,
                'status':status.HTTP_200_OK
            }
        )
    else:
        return Response(
            {
                'message':'Error updating choice',
                'status':status.HTTP_400_BAD_REQUEST,
            }
        )

#------------------------DELETE------------------------------------------
@api_view(['DELETE'])
def delete_question(request,id):
    question = Question.objects.get(id=id)
    question.delete()
    return Response(
        {
            'message':'Data deleted sucessfully'
        }
    )

@api_view(['DELETE'])
def delete_quiz(request,id):
    quiz = Quiz.objects.get(id=id)
    quiz.delete()
    return Response(
        {
            'message':'Data deleted sucessfully'
        }
    )g

@api_view(['DELETE'])
def delete_choice(request,id):
    choice = Choice.objects.get(id=id)
    choice.delete()
    return Response(
        {
            'message':'Data deleted sucessfully'
        }
    )
