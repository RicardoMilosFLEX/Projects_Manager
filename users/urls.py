from .views import *
from django.urls import path

urlpatterns = [
    path('', login, name='login'),
    path('register', register, name='register'),
]