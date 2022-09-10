from django.shortcuts import render,redirect
from .models import Chat

# Create your views here.
def index(request):
    chat=Chat.objects.all()
    context={
        'chat':chat
    }
    return render(request, 'application/index.html',context)

def new(request):
    return render(request, 'application/new.html')

def create(request):
    user=request.POST.get('user')
    content=request.POST.get('content')
    chat=Chat(user=user, content=content)
    chat.save()
    return redirect('application:index')

def detail(request, pk):
    chat=Chat.objects.get(pk=pk)
    context={
        'chat':chat,
        'prev':pk-1,
        'next':pk+1
    }
    return render(request, 'application/detail.html', context)

def delete(request, pk):
    chat=Chat.objects.get(pk=pk)
    chat.delete()
    return redirect('application:index')

def edit(request, pk):
    chat=Chat.objects.get(pk=pk)
    context={
        'chat':chat,
    }
    return render(request, 'application/edit.html', context)

def update(request, pk):
    chat=Chat.objects.get(pk=pk)
    chat.user=request.POST.get('user')
    chat.content=request.POST.get('content')
    chat.save()
    return redirect('application:detail',chat.pk)