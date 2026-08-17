from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import context
from food_menu.models import FoodItem
from food_menu.forms import FoodItemForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def index(request):
    food_items = FoodItem.objects.all()
    context =  {"food_items": food_items}
    return render(request, "food_menu/menu.html", 
                    context
                  )

def detail(request, item_id):
    food_item = FoodItem.objects.get(id=item_id)
    context = {"food_item": food_item}
    return render(request, "food_menu/detail.html", context)


def create_food_item(request):
  if request.method == 'POST':
    form = FoodItemForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return redirect('food_menu:index')
  else:
    form = FoodItemForm()
    context = {'form': form}
  return render(request, 'food_menu/create_item.html', context)

def update_food_item(request, item_id):
    food_item = FoodItem.objects.get(id=item_id)
    if request.method == 'POST':
        form = FoodItemForm(request.POST, request.FILES, instance=food_item)
        if form.is_valid():
            form.save()
            return redirect('food_menu:detail', item_id=food_item.id)
    else:
        form = FoodItemForm(instance=food_item)
    context = {'form': form, 'food_item': food_item}
    return render(request, 'food_menu/create_item.html', context)

def delete_food_item(request, item_id):
  food_item = FoodItem.objects.get(id=item_id)
  if request.method == "POST":
          food_item.delete()
          return redirect('food_menu:index')
  context = {"food_item": food_item}
  return render(request, "food_menu/delete_item.html", context)