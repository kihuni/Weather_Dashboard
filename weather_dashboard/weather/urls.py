from django.urls import path
from .views import weather_dashboard

urlpatterns = [
    path('', weather_dashboard, name='weather_dashboard'),
]