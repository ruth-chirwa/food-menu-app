from django.http import HttpResponse
from django.shortcuts import render
from food_menu.models import FoodItem
# Create your views here.

def index(request):
    food_items = FoodItem.objects.all()
    context =  {"food_items": food_items}
    return render(request, "food_menu/menu.html", 
                    context=context
                  )

def detail(request, item_id):
    food_item = FoodItem.objects.get(id=item_id)
    context = {"food_item": food_item}
    return render(request, "food_menu/detail.html", context=context)


def item(request):
    return HttpResponse("This is the item view.")