from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, "home.html", {})

# Create your views here.
def authView(request):
    if request.method == "POST":
        form =UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login:login")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})

def equipments(request):
    return render(request, "equipments.html")

def experiments(request):
    return render(request, "experiments.html")

def chemicals(request):
    return render(request, "chemicals.html")

def chatbot(request):
    return render(request, "chatbot.html")

def login_view(request):
    return render(request, 'login.html')

def signup_view(request):
    return render(request, 'signup.html')
