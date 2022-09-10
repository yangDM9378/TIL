from django.shortcuts import render

# Create your views here.
def calculator(request, first, second):
    Qo=first-second
    rhq=first*second
    
    if second==0:
        sk=9999
    else:
        sk=first/second

    content={
        'first':first,
        'second':second,
        'Qo':Qo,
        'rhq':rhq,
        'sk':sk,
    }
    return render(request, 'calculators/calculator.html', content)