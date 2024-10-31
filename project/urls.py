
from .views import *
from django.urls import path



urlpatterns = [
    path('', index, name='index'),
    path('/create', create, name='create'),
    path('/manage', manage, name='manage'),
]