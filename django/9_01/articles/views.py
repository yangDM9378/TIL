from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    name='금기륜'
    fruit_list=['귤','딸기','사과','감','바나나','파인애플']
    hate=['사과','구아바']
    context={
        'name':name,
        'fruit_list':fruit_list,
        'hate':hate,
    }
    return render(request, 'articles/index.html',context)


def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    message = request.GET.get('message')
    context={
        'message':message,
        }
    return render(request, 'articles/catch.html',context)


def main(request):
    articles=Article.objects.all()
    context ={
        'articles':articles,
    }
    return render(request, 'articles/main.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    article = Article(title=title, content=content)
    article.save()

    return redirect('articles:main')

def detail(request,pk):
    article = Article.objects.get(pk=pk)
    context={
        'article':article,
    }
    return render(request, 'articles/detail.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:main')

def edit(request, pk):
    article=Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    article=Article.objects.get(pk=pk)
    article.title=request.POST.get('title')
    article.content=request.POST.get('content')
    article.save()
    return redirect('articles:detail', article.pk)