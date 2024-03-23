from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Question, Choice

def home(request):
    questions = Question.objects.all()
    if request.method == 'POST':
        score = 0
        total_questions = Question.objects.count()
        for question in questions:
            selected_choice_id = request.POST.get(f'question{question.id}')
            correct_choice = Choice.objects.get(question=question, is_correct=True)
            if int(selected_choice_id) == correct_choice.id:
                score += 1
        messages.success(request, f'You scored {score} out of {total_questions}')
        return redirect('home')
    return render(request, 'home.html', {'questions': questions})