from django.shortcuts import render,redirect
from .models import Question, Comment
from .forms import QuestionForm, CommentForm
import random

# Create your views here.
def index(request):
    questions=Question.objects.all()
    context = {
        'questions':questions,
    }
    return render(request, 'eithers/index.html',context)


def create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            return redirect('eithers:detail', question.pk)
    else:
        form = QuestionForm()

    context = {
        'form' : form,
    }
    return render(request, 'eithers/create.html', context)
    

def detail(request,pk):
    question=Question.objects.get(pk=pk)
    comment_form=CommentForm()
    comments=question.comment_set.all()
    context={
        'question':question,
        'comment_form':comment_form,
        'comments':comments,
    }
    return render(request, 'eithers/detail.html', context)

def comments_create(request,pk):
    question=Question.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.question = question
        comment.save()
    return redirect('eithers:detail', question.pk)

def random2(request):
    questions=Question.objects.all()
    len_que=len(questions)
    q=random.randrange(1,len_que+1)
    quest=Question.objects.get(pk=q)
    return redirect('eithers:detail', quest.pk)