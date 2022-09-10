from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from django.views.decorators.http import require_http_methods, require_POST,require_safe
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles=Article.objects.all()
    context={
        'articles':articles,
    }
    return render(request, 'articles/index.html',context)


@require_http_methods(['GET','POST'])
def create(request):
    if request.method=='POST':
        form=ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:index')
    # 사용자가 처음으로 생성 페이지에 접근했을 때
    else:
        form=ArticleForm()
    context={
        'form':form,
    }
    return render(request, 'articles/create.html', context)

#read
@require_safe
def detail(request, pk):
    # get_object_or_404 = 데이터를 조회하지 못하면 404 에러를 띄워라!
    # 일반적으로 웹에서 없는 데이터 조회 시 404 에서를 띄움
    article=get_object_or_404(Article, pk=pk)
    context={
        'article':article,
    }
    
    return render(request, 'articles/detail.html',context)
#update
@require_http_methods(['GET','POST'])
def update(request, pk):
    article=get_object_or_404(Article,pk=pk)
    if request.method=='POST':
        form=ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form=ArticleForm(instance=article)
    context={
        'form':form,
        'article':article,
    }
    return render(request, 'articles/update.html', context)
#delete
@require_POST
def delete(request, pk):
    article=Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')