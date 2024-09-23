from django.shortcuts import render, redirect, get_object_or_404
from .models import Question, Choice, UserAnswer
from django.contrib.auth.decorators import login_required

def index(request):
    questions = Question.objects.all()
    return render(request, 'index.html', {'questions': questions})


@login_required
def vote(request, pk):
    question = get_object_or_404(Question, id=pk)
    options = question.choices.all()

    if request.method == 'POST':
        input_value = request.POST['choice']
        selected_choice = get_object_or_404(Choice, id=input_value, question=question)
        UserAnswer.objects.update_or_create(
            user=request.user,
            question=question,
            defaults={'selected_choice': selected_choice}
        )
        return redirect('final_result')  

    return render(request, 'vote.html', {'question': question, 'options': options})

def result(request, pk):
    question = get_object_or_404(Question, id=pk)
    options = question.choices.all()
    total_votes = sum(option.vote for option in options)
    user_answer = UserAnswer.objects.filter(user=request.user, question=question).first()

    return render(request, 'result.html', {
        'question': question,
        'options': options,
        'user_answer': user_answer,
        'total_votes': total_votes,
    })
def result_view(request):
    answers = UserAnswer.objects.filter(user=request.user)
    total_score = sum(answer.selected_choice.value for answer in answers if answer.selected_choice)

    return render(request, 'result.html', {'total_score': total_score})
