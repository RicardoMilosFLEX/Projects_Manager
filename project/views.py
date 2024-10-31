from django.shortcuts import render

def index(request):
    '''
    Метод возвращает отображение главной страницы
    :param request:
    :return: basic.html
    '''
    return render(request, 'project/basic.html')


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