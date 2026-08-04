from django.http import HttpResponse
from django.shortcuts import render
from food_menu.models import FoodItem
# Create your views here.

def index(request):
    food_items = FoodItem.objects.all()
    return render(request, "food_menu/menu.html", 
                  {"food_items": food_items}
                  )


def item(request):
    return HttpResponse("This is the item view.")