from django.urls import path
from . import views

app_name = "food_menu"

urlpatterns = [
    path('', views.IndexClassView.as_view(), name='index'),
    path('detail/<int:pk>/', views.FoodDetailClassView.as_view(), name='detail'),
    path('add/', views.CreateFoodItemClassView.as_view(), name='create_food_item'),
    path('update/<int:pk>/', views.UpdateClassView.as_view(), name='update_food_item'),
    path('delete/<int:pk>/', views.DeleteClassView.as_view(), name='delete_food_item'),
]
