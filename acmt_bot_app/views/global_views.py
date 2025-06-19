from django.shortcuts import render
# from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, "home.html")


def login_view(request):
    return render(request, "login.html")

def kode_otp_view(request):
    return render(request, "kode_otp.html")

def forgot_password_view(request):
    return render(request, "forgot_password.html")

def create_new_password_view(request):
    return render(request, "create_new_pass.html")

def success_reset_password_view(request):
    return render(request, "success_reset_pass.html")
    