from django.urls import path
from django.contrib import admin
from acmt_bot_app.views import global_views as views
# from ..views import global_views as views

urlpatterns = [
    path('', views.home, name='home'),

    # LOGIN
    path('login/', views.login_view, name='login'),

    #Kode OTP
    path('kode-otp/', views.kode_otp_view, name='kode-otp'),

    #Forgot Password
    path('forgot-password/', views.forgot_password_view, name='forgot-password'),

    #Reset Password
    path('create-new-password/', views.create_new_password_view, name='create-new-password'),

    #Success Reset Password
    path('success-reset-password/', views.success_reset_password_view, name='success-reset-password'),
]