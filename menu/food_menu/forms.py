from django import forms
from food_menu.models import FoodItem

class FoodItemForm(forms.ModelForm):

   class Meta:  
    model = FoodItem
    fields = ['name', 'description', 'price', 'image']