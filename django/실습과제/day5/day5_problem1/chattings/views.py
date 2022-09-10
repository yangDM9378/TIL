from django.shortcuts import render,redirect
from django.views.decorators.http import require_safe, require_http_methods, require_POST
from .models import Chat
from .forms import ChatForm

# Create your views here.
@ require_safe
def index(request):
    chat=Chat.objects.all()
    context={
        'chats':chat,
    }
    return render(request, 'chattings/index.html', context)

@require_http_methods(['POST','GET'])
def create(request):
    if request.method=='POST':
        form=ChatForm(request.POST)
        if form.is_valid():
            chat=form.save()
            return redirect('chattings:detail', chat.pk)
    else:
        form=ChatForm()
    context={
        'form':form,
    }
    return render(request, 'chattings/create.html',context)

@require_safe
def detail(request,pk):
    chat=Chat.objects.get(pk=pk)
    context={
        'chat':chat,
    }
    return render(request, 'chattings/detail.html',context)

@require_POST
def delete(request,pk):
    chat=Chat.objects.get(pk=pk)
    chat.delete()
    return redirect('chattings:index')