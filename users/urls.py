
from .views import *
from django.urls import path

urlpatterns = [
    path('login', login, name='login'),
    path('register', register, name='register'),
    path('logout', logout, name='logout'),
    path('change_user/<int:worker_id>/', change_user, name='change_user'),
    path('users_list', show_users, name='show_users'),
    path('delete_user/<int:worker_id>/', show_delete_user, name='show_delete_user'),
    path('delete_user/<int:worker_id>/delete', delete_user, name='delete_user'),
]