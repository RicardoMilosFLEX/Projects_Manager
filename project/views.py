from lib2to3.fixes.fix_input import context

from django.urls import reverse

from django.http import HttpResponseRedirect

from django.shortcuts import render, get_object_or_404

from project.forms import ProjectForm, TaskForm, ChangeProjectForm
from project.models import Projects, Tasks, TaskLists
from users.models import Workers, Responsible


def index(request):
    '''
    Метод возвращает отображение главной страницы
    :param request:
    :return: basic.html
    '''
    return render(request, 'project/basic.html')
def show_project(request):
    '''
    Метод отображения проектов
    :param request:
    :return: project.html
    '''
    users = Workers.objects.all()
    projects = Projects.objects.all()
    context = {'users': users, 'projects': projects}
    return render(request, 'project/project.html', context)
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

def change_project(request, project_id):
    '''
    Метод возвращает страницу для изменения проетка для администратора
    :param request:
    :param project_id:
    :return:
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

    :param request:
    :return:
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

def show_projects_for_managers(request, manager_id):
    '''
    Отображает проекты для конкретного менеджера
    :param request:
    :return:
    '''
    projects = Projects.objects.filter(responsible=manager_id)
    context = {'projects': projects}
    return render(request, 'project/show_projects_for_managers.html', context)


def show_tasks_for_managers(request, task_list):
    '''Отображение задач по проекту для менеджеров'''
    list_id = get_object_or_404(TaskLists, list_name=task_list)
    tasks = Tasks.objects.filter(list=list_id)
    context = {'tasks': tasks}
    return render(request, 'project/show_tasks.html', context)