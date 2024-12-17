from django.db.models.fields import return_None
from django.urls import reverse

from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render, get_object_or_404

from project.forms import ProjectForm, TaskForm, ChangeProjectForm, ChangeTaskForm
from project.models import Projects, Tasks, TaskLists
from users.models import Workers, Responsible


def index(request):
    '''
    Метод возвращает отображение главной страницы
    :param request:
    :return: basic.html
    '''
    return render(request, 'project/basic.html')
def show_all_managers(request):
    '''
    Метод отображения менеджеров для администраторов
    :param request:
    :return:
    '''
    managers = Responsible.objects.all()
    projects = Projects.objects.all()
    context = {
        'managers': managers,
        'projects': projects,
    }
    return render(request, 'project/manager_info.html', context)
def create_project(request):
    '''
    Метод возвращает страницу по созданию проекта (для администраторов)
    :param request:
    :return: create_project.html
    '''
    if request.method == 'POST':
        form = ProjectForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('projects'))
        else:
            print(form.errors)
    else:
        form = ProjectForm()

    context = {'start_project_form': form}
    return render(request, 'project/create_project.html', context)

def sort_projects(request):
    '''
    Отображение и Сортировка проектов по критериям пользователя (администратора)
    :param request:
    :return:
    '''
    sort_by = request.GET.get('sort_by', 'project_name')

    ALLOWED_SORT_FIELDS = {
        'project_name': 'Название проекта',
        'status':'Статус',
        'plan_start_date': 'Дата начала',
        'plan_finish_date': 'Дата окончания',
    }
    if sort_by not in ALLOWED_SORT_FIELDS:
        sort_by = 'project_name'

    projects = Projects.objects.all().order_by(sort_by)
    users = Workers.objects.all()
    context = {'projects': projects,
               'sort_by': sort_by,
               'users': users,
               'sort_fields': ALLOWED_SORT_FIELDS,}
    return render(
        request,
        'project/project.html',context
    )

def change_project(request, project_id):
    '''
    Метод возвращает страницу для изменения проетка для администратора
    :param request:
    :param project_id:
    :return: change_project.html
    '''
    project = get_object_or_404(Projects, pk=project_id)
    if request.method == 'POST':
        form = ChangeProjectForm(data=request.POST, instance=project)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('projects'))
    else:

        form = ChangeProjectForm(instance=project)
    context = {'change_project_form': form}
    return render(request, 'project/change_project.html', context)
def create_task(request):
    '''
    Обработка создания задач для проектов (для менеджеров)
    :param request:
    :return: create_project.html
    '''
    if request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            print(form.errors)
    else:
        form = TaskForm()
    context = {'start_task_form': form}
    return render(request, 'project/create_tasks.html', context)

def change_task(request, task_id):
    '''
    Отображает форму для изменения задачи для менеджера
    :param request:
    :param task_id:
    :return:
    '''
    task = get_object_or_404(Tasks, pk=task_id)
    task_list = get_object_or_404(TaskLists, pk=task_id)
    if request.method == 'POST':
        form = ChangeTaskForm(data=request.POST, instance=task)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('show_tasks_list', args=[task_list]))
    else:
        form = ChangeTaskForm(instance=task)
    context = {
        'change_task_form': form,
               }
    return render(request, 'project/change_task.html', context)
def show_projects_for_managers(request, manager_id : int):
    '''
    Отображает и сортирует проекты для конкретного менеджера
    :param request:
    :param manager_id: int
    :return: show_projects_for_managers.html
    '''
    sort_by = request.GET.get('sort_by', 'project_name')
    ALLOWED_SORT_FIELDS = {
        'project_name': 'Название',
        'status': 'Статус',
        'plan_start_date': 'Дата начала проекта',
        'plan_finish_date': 'Дата окончания проекта',
        'type': 'Тип проекта',
    }
    if sort_by not in ALLOWED_SORT_FIELDS:
        sort_by = 'project_name'
    projects = Projects.objects.filter(responsible=manager_id).order_by(sort_by)
    context = {'projects': projects,
               'sort_by': sort_by,
               'sort_fields': ALLOWED_SORT_FIELDS,}
    return render(request, 'project/show_projects_for_managers.html', context)


def show_tasks_for_managers(request, task_list):
    '''
    Отображает и сортирует задачи по проекту для менеджеров
    :param request:
    :param task_list:
    :return: show_projects_for_managers.html
    '''
    sort_by = request.GET.get('sort_by', 'description')
    ALLOWED_SORT_FIELDS = {
        'description': 'Описание',
        'start_date': 'Дата начала',
        'plan_finish_date': 'Дата окончания',
        'status':'Статус',
        'priority':'Приоритет',
    }
    if sort_by not in ALLOWED_SORT_FIELDS:
        sort_by = 'description'
    list_id = get_object_or_404(TaskLists, list_name=task_list)
    tasks = Tasks.objects.filter(list=list_id).order_by(sort_by)
    context = {'tasks': tasks,
               'sort_by': sort_by,
               'sort_fields': ALLOWED_SORT_FIELDS,}
    return render(request, 'project/show_tasks.html', context)

def delete_project(request, project_id):
    '''
    Удаление проектов
    :param request:
    :param project_id:
    :return:
    '''
    project = get_object_or_404(Projects, pk=project_id)
    if request.method == 'POST':
        project.delete()
        messages.success(request, "Проект успешно удалён.")
    return HttpResponseRedirect(reverse('projects'))

def delete_task(request, task_id):
    '''
    Удаление задач
    :param request:
    :param task_id:
    :return:
    '''
    task = get_object_or_404(Tasks, pk=task_id)
    if request.method == 'POST':
        task.delete()
        messages.success(request,'Задача успешно удалена.')
    return HttpResponseRedirect(reverse('index'))