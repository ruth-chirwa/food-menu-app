from django.urls import path
from . import views

app_name = "food_menu"

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:item_id>/', views.detail, name='detail'),
    path('add/', views.create_food_item, name='create_food_item'),
]
