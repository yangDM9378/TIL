from email.policy import default
from django.shortcuts import render

# Create your views here.
def first(request):
    catch_thrid_throw=request.POST.get('third_throw')
    if catch_thrid_throw==None:
        catch_thrid_throw='noting'
    context={
        'catch_third_throw':catch_thrid_throw,
    }
    return render(request, 'throw_loops/first.html', context)

def second(request):
    catch_first_throw=request.POST.get('first_throw')
    context={
        'catch_first_throw':catch_first_throw,
    }
    return render(request, 'throw_loops/second.html', context)

def third(request):
    catch_second_throw1=request.POST.get('second_throw_1')
    catch_second_throw2=request.POST.get('second_throw_2')
    context={
        'catch_second':[catch_second_throw1,catch_second_throw2]
    }

    return render(request, 'throw_loops/third.html', context)