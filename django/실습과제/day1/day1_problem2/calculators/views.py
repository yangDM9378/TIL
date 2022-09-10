from django.shortcuts import render

# Create your views here.
def result(request):
    first=request.GET.get('firstnum')
    second=request.GET.get('secondnum')
    a=int(first)
    b=int(second)
    Qo=a-b
    rhq=a*b
    if b!=0:
        sk=a/b
    else:
        sk='X'
    context={
        'first':a,
        'second':b,
        'Qo':Qo,
        'rhq':rhq,
        'sk':sk,
    }
    return render(request, 'result.html', context)

def calculation(request):
    return render(request, 'calculation.html')