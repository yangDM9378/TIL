from django.shortcuts import render

# Create your views here.
def food(request):
    food=['피자','치킨','국밥','초밥','민초흑당로제마라탕']
    context={
        'food':food,
    }
    return render(request, 'menus/food.html', context)

def drink(request):
    drink=['cider','coke','miranda','fanta','eye of finetree']
    drink_up=[i.capitalize() for i in drink]
    context={
        'drink':drink_up,
    }
    return render(request, 'menus/drink.html',context)


def receipt(request):
    menu=request.POST.get('order')
    food=['피자','치킨','국밥','초밥','민초흑당로제마라탕']
    drink=['cider','coke','miranda','fanta','eye of finetree']
    drink_up=[i.capitalize() for i in drink]
    mix_menu=food+drink_up
    result=menu.capitalize()
    context={
        'menu':result,
        'mix_menu':mix_menu
    }

    return render(request, 'menus/receipt.html',context)

