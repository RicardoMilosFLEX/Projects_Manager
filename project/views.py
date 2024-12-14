from lib2to3.fixes.fix_input import context

from django.urls import reverse

from django.http import HttpResponseRedirect

from django.shortcuts import render

from project.forms import ProjectForm, TaskForm
from project.models import Projects
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
    return render(request, 'project/project.html', {'projects': projects,'users':users})
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

def manage(request):
    '''
    Метод возвращает страницу для изменения данных в проекте
    :param request:
    :return:
    '''
    pass

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