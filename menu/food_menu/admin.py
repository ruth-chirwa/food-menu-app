from django.contrib import admin
from food_menu.models import FoodItem
# Register your models here.
@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "price",
    )
    ordering = ("name",)
    search_fields = ("name", "description")
    list_filter = ("price",)

    fieldsets = (
        ("Basic Information", {"fields": ("name", "description")}),
        ("Pricing", {"fields": ("price",)}),
    )