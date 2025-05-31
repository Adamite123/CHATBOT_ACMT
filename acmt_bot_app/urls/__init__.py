from django.urls import include, path

urlpatterns = [
    path('', include('acmt_bot_app.urls.global_urls')),
]
