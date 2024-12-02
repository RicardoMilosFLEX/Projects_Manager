from django.shortcuts import render

from project.models import Projects


def index(request):
    '''
    Метод возвращает отображение главной страницы
    :param request:
    :return: basic.html
    '''
    return render(request, 'project/basic.html')
def show_project(request):
    projects = Projects.objects.all()
    return render(request, 'project/project.html', {'projects': projects})

def create(request):
    '''
    Метод возвращает страницу по созданию проекта
    :param request:
    :return: create.html
    '''
    pass

def manage(request):
    '''
    Метод возвращает страницу для изменения данных в проекте
    :param request:
    :return:
    '''
    pass