from django.contrib import admin
from authentication.models import Profile
# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "image",
        "location",
    )
    search_fields = (
        "user",
        "location",
    )
    ordering = ["user"]
    list_filter = (
        "user",
        "location",
    )

    fieldset = (
        ("Ownsership", {"fields":(
            "user",
            "image",
            "location",)})
    )