from django.shortcuts import render, redirect
from .forms import RegisterForm
from store.models import*

# Create your views here.

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            user = form.save()
            Customer.objects.create(user=user, name=Customer.name, email=user.email)

        return redirect("/")
    else:
        form = RegisterForm()
    return render(response, "register/register.html", {"form":form})