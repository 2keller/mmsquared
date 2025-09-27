from django.urls import path
from . import views # Correctly imports views.py

urlpatterns = [
    # Maps the root URL ('/') to views.home
    path('', views.home, name='home'),
    
    # Maps service URLs to their corresponding view functions
    path('photography/', views.photography, name='photography'),
    path('printing/', views.printing, name='printing'),
    path('tutoring/', views.tutoring, name='tutoring'),
]