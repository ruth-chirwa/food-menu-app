from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def register(request):
    form = UserCreationForm()
    context = {"form": form }
    if request.method == "POST":
        form = UserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            user_name = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {user_name}")
            return redirect("food_menu:index")
        
    return render(request, "authentication/register.html", context)