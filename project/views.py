
import json
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from project.forms import ProjectForm, TaskForm, ChangeProjectForm, ChangeTaskForm
from project.models import Projects, Tasks, TaskLists
from users.models import Workers, Responsible
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from .models import Tasks
from .decorators import admin_required, manager_required, worker_required

def index(request):
    '''
    Метод возвращает отображение главной страницы в зависимости от роли пользователя
    :param request:
    :return: соответствующий шаблон
    '''
    if request.user.is_authenticated:
        if request.user.position_id == 1:  # Администратор
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
            context = {
                'projects': projects,
                'sort_by': sort_by,
                'users': users,
                'sort_fields': ALLOWED_SORT_FIELDS,
            }
            return render(request, 'project/project.html', context)
        elif request.user.position_id == 2:  # Менеджер
            return HttpResponseRedirect(reverse('check_projects_for_manager', args=[request.user.worker_id]))
        else:  # Рабочий
            return HttpResponseRedirect(reverse('show_tasks_for_workers', args=[request.user.worker_id]))
    return render(request, 'project/main_page.html')
def main(request):
    '''
    Метод возвращает главную страницу в зависимости от роли пользователя
    :param request:
    :return: соответствующий шаблон
    '''
    return render(request, 'project/main_page.html')
@admin_required
def show_all_managers(request):
    sort_by = request.GET.get('sort_by', 'surname')  # По умолчанию сортировка по фамилии
    
    ALLOWED_SORT_FIELDS = {
        'surname': 'Фамилия',
        'name': 'Имя',
        'email': 'Email',
    }
    
    if sort_by not in ALLOWED_SORT_FIELDS:
        sort_by = 'surname'
        
    managers = Responsible.objects.all().order_by(sort_by)
    projects = Projects.objects.all()
    
    context = {
        'managers': managers,
        'projects': projects,
        'sort_by': sort_by,
        'sort_fields': ALLOWED_SORT_FIELDS,
    }
    
    return render(request, 'project/manager_info.html', context)
@admin_required
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

@admin_required
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

@admin_required
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
        initial_data = {
            'plan_start_date': project.plan_start_date,
            'plan_finish_date': project.plan_finish_date
        }
        form = ChangeProjectForm(instance=project, initial=initial_data)
    context = {'change_project_form': form, 'project': project}
    return render(request, 'project/change_project.html', context)
@manager_required
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
@manager_required
def change_task(request, task_id):
    '''
    Отображает форму для изменения задачи для менеджера
    :param request:
    :param task_id:
    :return:
    '''
    task = get_object_or_404(Tasks, pk=task_id)
    task_list = task.list
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
@manager_required
def show_projects_for_managers(request, manager_id : int):
    '''
    Отображает и сортирует проекты для конкретного менеджера
    :param request:
    :param manager_id: int
    :return: show_projects_for_managers.html
    '''
    if request.user.worker_id != manager_id:
        return HttpResponseRedirect(reverse('index'))
    
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

@manager_required
def show_tasks_for_managers(request, task_list):
    '''
    Отображает и сортирует задачи по проекту для менеджеров
    :param request:
    :param task_list:
    :return: show_projects_for_managers.html
    '''
    list_id = get_object_or_404(TaskLists, list_name=task_list)
    project = Projects.objects.filter(tasks_list=list_id).first()
    if not project or project.responsible.responsible_id != request.user.worker_id:
        messages.error(request, 'У вас нет доступа к этим задачам')
        return HttpResponseRedirect(reverse('index'))
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
@worker_required
def show_and_sort_tasks_for_workers(request, worker_id):
    sort_by = request.GET.get('sort_by', 'priority')
    ALLOWED_SORT_FIELDS = {
        'description': 'Описание',
        'plan_finish_date': 'Дата окончания',
        'status': 'Статус',
        'priority': 'Приоритет',
    }
    if sort_by not in ALLOWED_SORT_FIELDS:
        sort_by = 'priority'
    tasks = Tasks.objects.filter(responsible_worker=worker_id).order_by(sort_by)
    context = {'tasks': tasks,
               'sort_by': sort_by,
               'sort_fields': ALLOWED_SORT_FIELDS,}
    return render(request, 'project/show_tasks_for_worker.html', context)
@worker_required
def show_project_for_worker(request, worker_id):
    '''
    Отображение проекта над которым работает разработчик
    :param request:
    :param worker_id:
    :return: show_project_for_worker.html
    '''
    sort_by = request.GET.get('sort_by', 'project_name')
    ALLOWED_SORT_FIELDS = {
        'project_name': 'Название',
        'status': 'Статус',
        'plan_finish_date': 'Дата окончания проекта',
        'type': 'Тип проекта',
    }
    if sort_by not in ALLOWED_SORT_FIELDS:
        sort_by = 'project_name'
    tasks = Tasks.objects.filter(responsible_worker_id=worker_id)
    tasks_lists = [tasks.list for tasks in tasks]
    projects = Projects.objects.filter(tasks_list__in=tasks_lists)
    context = {'projects': projects,
               'sort_by': sort_by,
               'sort_fields': ALLOWED_SORT_FIELDS,}
    return render(request, 'project/show_project_for_worker.html', context)
@worker_required
def update_task_status(request, task_id):
    '''
    Метод обновляет статус задачи
    :param request:
    :param task_id:
    :return: redirect на страницу задач
    '''
    if request.method == 'POST':
        task = get_object_or_404(Tasks, pk=task_id)
        new_status_id = request.POST.get('status')
        if new_status_id:
            task.status_id = new_status_id
            task.save()
        return redirect('show_tasks_for_workers', worker_id=request.user.worker_id)
    return redirect('show_tasks_for_workers', worker_id=request.user.worker_id)
@manager_required
def update_project_status(request, project_id):
    '''
    Метод обновляет статус проекта
    :param request:
    :param project_id:
    :return: redirect на страницу проектов
    '''
    if request.method == 'POST':
        project = get_object_or_404(Projects, pk=project_id)
        new_status_id = request.POST.get('status')
        if new_status_id:
            project.status_id = new_status_id
            project.save()
        return redirect('check_projects_for_manager', manager_id=request.user.worker_id)
    return redirect('check_projects_for_manager', manager_id=request.user.worker_id)
@admin_required
def show_delete_project(request, project_id):
    '''
    Метод возвращает страницу для удаления проекта
    :param request:
    :return: delete_project.html
    '''
    project = get_object_or_404(Projects, pk=project_id)
    context = {'project': project}
    return render(request, 'project/delete_project.html', context)
@manager_required
def show_delete_task(request, task_id):
    """Метод возвращает страницу для удаления задачи

    Args:
        request (request): запрос
        task_id (int): id задачи

    Returns:
        render: страница для удаления задачи
    """
    task = get_object_or_404(Tasks, pk=task_id)
    context = {'task': task}
    return render(request, 'project/delete_tasks.html', context)
@admin_required
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
@manager_required
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

def show_calendar(request, worker_id):
    # Пока не работает
    '''
    Отображает календар с датами для разработчиков
    :param request:
    :param worker_id:
    :return:
    '''
    tasks = Tasks.objects.filter(responsible_worker_id=worker_id)
    events = []
    for task in tasks:
        event = {
            'title': task.description,
            'end': task.plan_finish_date.strftime('%Y-%m-%d'),
            'status': task.status.status_name,
            'priority': task.priority.priority_name,
        }
        events.append(event)

    events_json = json.dumps(events)
    context = {'events': events_json}
    return render(request, 'project/calendar_page.html', context)




def generate_pdf(request):

    tasks = Tasks.objects.all()

    template = get_template('project/report.html')
    html = template.render({'tasks': tasks})

    font_path = 'project/static/img/DejaVuSans.ttf'
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="report.pdf"'

    pisa_status = pisa.CreatePDF(html, dest=response, font_path=font_path)

    if pisa_status.err:
        return HttpResponse('Ошибка при генерации PDF', status=500)

    return response
