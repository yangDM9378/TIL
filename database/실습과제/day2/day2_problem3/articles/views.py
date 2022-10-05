from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from .models import Article,Comment
from .forms import ArticleForm,CommentForm

# Create your views here.
@require_safe
def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


@require_http_methods(['GET', 'POST'])
def create(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ArticleForm(request.POST)
            if form.is_valid():
                article = form.save(commit=False)
                article.author = request.user
                article.save()
                return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm()
        context = {
            'form': form,
        }
        return render(request, 'articles/create.html', context)
    return redirect('accounts:login')


@require_safe
def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comment_form=CommentForm()
    comments=article.comment_set.all()
    context = {
        'article': article,
        'comment_form':comment_form,
        'comments':comments,
    }
    return render(request, 'articles/detail.html', context)


@require_POST
def delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.user.is_authenticated:
        if request.user == article.author:
            article.delete()
        return redirect('articles:index')
    return redirect('accounts:login')



@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.user==article.author:
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                form.save()
                return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm(instance=article)
    else:
        return redirect('accounts:login')
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)

def comments_create(request,pk):
    article=Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article=article
        comment.author=request.user
        comment.save()
    return redirect('articles:detail',article.pk)

def comments_delete(request, article_pk, comment_pk):
    comment=Comment.objects.get(pk=comment_pk)
    if request.user == comment.author:
        comment.delete()
    return redirect('articles:detail', article_pk)