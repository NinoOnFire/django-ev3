from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import RegistroForm

# Create your views here.

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) 
            return redirect("inicio") 
        else:
            messages.error(request, "Usuario o contraseña incorrectos")
    
    return render(request, "login.html")

from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect("login")

def registro(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("galeria")  
    else:
        form = RegistroForm()
    return render(request, "registro.html", {"form": form})
