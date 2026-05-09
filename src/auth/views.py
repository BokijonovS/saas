from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your views here.

def loginview(request):
    if request.method == "POST":
        username = request.POST.get("username") or None
        password = request.POST.get("password") or None
        # username = "admin"
        # password = "admin"
        if all([username, password]):
            user = authenticate(request, username=username,
                                password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
    return render(request, "auth/login.html", {})


def registerview(request):
    if request.method == "POST":
        username = request.POST.get("username") or None
        email = request.POST.get("email") or None
        password = request.POST.get("password") or None
    return render(request, "auth/register.html", {})

