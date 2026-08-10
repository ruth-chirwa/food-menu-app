from django.shortcuts import redirect, render
from django.contrib import messages
from authentication.forms import RegistrationForm

# Create your views here.
def register(request):
    form = RegistrationForm()
   
    if request.method == "POST":
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            user_name = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {user_name}")
            return redirect("food_menu:index")
        else:
            print(form.errors)
    context = {"form": form }  
    return render(request, "authentication/register.html", context)