from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User, Group
from django.shortcuts import render
import environ

# Initialise environment variables
env = environ.Env()
environ.Env.read_env()

auth = { "Authorization": "Token " + env("TOKEN") }

def home(request): 
    return render(request, "main/home.html")

@login_required(login_url="/login")
def free(request): 
    return render(request, "main/free.html", auth)

@login_required(login_url="/login")
def pro(request): 
    if request.user.groups.filter(name="test"):
        return render(request, "main/pro.html", auth)
    else:
        return render(request, "main/get_pro.html", auth)

def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegisterForm()
    return render(request, 'registration/sign_up.html', {"form": form})