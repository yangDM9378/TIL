from django.shortcuts import render, redirect
from .models import Movies
from .forms import MoviesForm
from django.views.decorators.http import require_http_methods,require_POST,require_safe

# Create your views here.
@require_safe
def index(request):
    movies=Movies.objects.all()
    context={
        'movies':movies,
    }
    return render(request, 'movies/index.html', context)

@require_http_methods(['POST','GET'])
def create(request):
    if request.method=='POST':
        form=MoviesForm(request.POST)
        if form.is_valid():
            movie=form.save()
            return redirect('movies:index')
    else:
        form=MoviesForm()
    context={
        'form':form,
    }    
    return render(request, 'movies/create.html', context)

@require_safe
def detail(request,pk):
    movies=Movies.objects.get(pk=pk)
    context={
        'movies':movies,
    }
    return render(request, 'movies/detail.html', context)

def delete(request, pk):
    movie=Movies.objects.get(pk=pk)
    movie.delete()
    return redirect('movies:index')

def update(request, pk):
    movie=Movies.objects.get(pk=pk)
    if request.method =='POST':
        form = MoviesForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form=MoviesForm(instance=movie)
    context={
        'movie':movie,
        'form':form,
    }
    return render(request,'movies/update.html',context)