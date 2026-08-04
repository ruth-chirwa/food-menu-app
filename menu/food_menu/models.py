from django.db import models

# Create your models here.
class FoodItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} - MWK{self.price}"