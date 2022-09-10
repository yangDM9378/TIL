from re import L
from django.shortcuts import render

# Create your views here.
def price(request, thing, cnt):
    product_price = {
        "라면":980,
        "홈런볼":1500,
        "칙촉":2300, 
        "식빵":1800,
        }
    if thing in product_price.keys():
        for i in product_price.items():
            if thing==i[0]:
                total=cnt*i[1]
    else:
        total=-1
        thing=thing
    
    content={
        'thing':thing,
        'total':total,
        'cnt':cnt,
    }
    print(content)

    return render(request, 'prices/price.html',content)