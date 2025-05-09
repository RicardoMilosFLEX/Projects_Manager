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
    path('show_tasks/<int:worker_id>', show_and_sort_tasks_for_workers, name='show_tasks_for_workers'),
    path('show_worker_project/<int:worker_id>', show_project_for_worker, name='show_worker_project'),
    path('show_delete_project/<int:project_id>', show_delete_project, name='show_delete_project'),
    path('delete_project/<int:project_id>', delete_project, name='delete_project'),
    path('delete_task/<int:task_id>', delete_task, name='delete_task'),
    path('calendar/<int:worker_id>', show_calendar, name='show_calendar'),
    path('generate-report/', generate_pdf, name='generate_pdf'),
]