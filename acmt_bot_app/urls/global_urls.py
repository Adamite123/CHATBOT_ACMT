from django.urls import path
from django.contrib import admin
from acmt_bot_app.views import global_views as views
# from ..views import global_views as views

urlpatterns = [
    path('', views.home, name='home'),

    # LOGIN
    path('login/', views.login_view, name='login'),

    #TES
    path('tes/', views.tes_view, name='tes'),
]