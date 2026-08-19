from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.
class FoodItem(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.CharField(max_length=600, default="https://img.freepik.com/premium-psd/plate-food-with-variety-ingredients-transparent-background_679658-77415.jpg")

    def __str__(self):
        return f"{self.name} - MWK{self.price}"


    def get_absolute_url(self):
        return reverse('food_menu:index')