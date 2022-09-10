from django.shortcuts import render,redirect, get_object_or_404
from .forms import TravelsForm
from .models import travels
from django.views.decorators.http import require_safe, require_POST, require_http_methods

# Create your views here.

@require_safe
def index(request):
    k=travels.objects.all()
    context={
        'travels':k,
    }
    return render(request,'travels/index.html',context)

@require_http_methods(['POST','GET'])
def create(request):
    if request.method=='POST':
        form=TravelsForm(request.POST)
        if form.is_valid():
            travel=form.save()
            return redirect('travels:detail', travel.pk)
    else:
        form=TravelsForm()
    context={
        'form':form,
    }
    return render(request, 'travels/create.html', context)

@require_safe
def detail(request, pk):
    error=get_object_or_404(travels, pk=pk)
    travel=travels.objects.get(pk=pk)
    context={
        'travel':travel,
        'error':error,
    }
    return render(request, 'travels/detail.html', context)

@require_POST
def delete(request, pk):
    travel=travels.objects.get(pk=pk)
    travel.delete()
    return redirect('travels:index')

@require_http_methods(['POST','GET'])
def update(request, pk):
    error=get_object_or_404(travels, pk=pk)
    travel=travels.objects.get(pk=pk)
    if request.method=='POST':
        form=TravelsForm(request.POST, instance=travel)
        if form.is_valid():
            form.save()
            return redirect('travels:detail',travel.pk)
    else:
        form=TravelsForm(instance=travel)
    context={
        'travel':travel,
        'form':form,
        'error':error,
    }
    return render(request,'travels/update.html', context)