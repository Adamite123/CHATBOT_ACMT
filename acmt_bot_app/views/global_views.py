from django.shortcuts import render
# from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, "home.html")


def login_view(request):
    return render(request, "loginv2.html")

def forgot_password_view(request):
    return render(request, "forgot_password.html")

def tes_view(request):
    return render(request, "tes.html")
    