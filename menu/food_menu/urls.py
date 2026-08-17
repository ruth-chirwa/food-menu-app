from django.urls import path
from . import views

app_name = "food_menu"

urlpatterns = [
    path('', views.IndexClassView.as_view(), name='index'),
    path('detail/<int:pk>/', views.FoodDetailClassView.as_view(), name='detail'),
    path('add/', views.create_food_item, name='create_food_item'),
    path('update/<int:item_id>/', views.update_food_item, name='update_food_item'),
    path('delete/<int:item_id>/', views.delete_food_item, name='delete_food_item'),
]
