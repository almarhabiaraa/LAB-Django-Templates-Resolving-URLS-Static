from django.urls import path
from . import views

app_name = "main"


# URL patterns for the main app (mapping URLs to views)
urlpatterns = [
    path('', views.home_view, name="home"),
    path('terms/', views.terms_view, name="terms"),
]
