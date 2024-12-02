
from django.contrib import admin
from django.urls import path, include
from project.urls import *
from users.urls import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('project.urls')),
    path('login/', include('users.urls')),
]
