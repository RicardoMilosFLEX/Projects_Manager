from .views import *
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('projects', sort_projects, name='projects'),
    path('create_project', create_project, name='create_project'),
    path('change_project/<int:project_id>', change_project, name='change_project'),
    path('managers_info', show_all_managers, name='managers_info' ),
    path('create_task', create_task, name='create_task'),
    path('change_task/<int:task_id>', change_task, name='change_task'),
    path('show_project/<int:manager_id>', show_projects_for_managers, name='check_projects_for_manager'),
    path('show_project/tasks_list/<str:task_list>', show_tasks_for_managers, name='show_tasks_list'),
]