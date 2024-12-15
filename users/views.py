
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib import auth
from django.urls import reverse
from django.contrib.auth import login

from users.forms import EmailAuthenticationForm, CustomUserCreationForm, ChangeUser
from users.models import Workers

import logging
def login(request):
    '''Авторизация пользователя'''
    if request.method == 'POST':
        form = EmailAuthenticationForm(data=request.POST)
        if form.is_valid():
            email = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=email, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                form.add_error(None, 'Неверные пароль или email')
    else:
        form = EmailAuthenticationForm()

    context = {'login_form': form}
    return render(request, 'users/Login.html', context)

def show_and_sort_users(request):
    '''
    Метод для отображения пользователей и их сортировки
    :param request:
    :return:
    '''
    sort_by = request.GET.get('sort_by', 'last_name')

    ALLOWED_SORT_FIELDS = {
        'last_name': 'Фамилия',
        'first_name': 'Имя',
        'position': "Должность",
    }
    if sort_by not in ALLOWED_SORT_FIELDS:
        sort_by = 'last_name'
    workers = Workers.objects.all().order_by(sort_by)
    context = {'workers': workers,
               'sort_by': sort_by,
               'sort_fields': ALLOWED_SORT_FIELDS
               }
    return render(request, 'users/users_list.html', context)


# ЭТОТ КОД НУЖНО ИСПРАВИТЬ. РАБОТАЕТ НЕ СОВСЕМ КОРРЕКТНО
logging.basicConfig(level=logging.INFO, filename="views.py",filemode="w")
logger = logging.getLogger(__name__)
# ЛОГИ УБРАТЬ в другой файл ПОТОМ
def change_user(request, worker_id):
    '''Редактирование пользователя'''
    logger.info(f"Текущий пользователь: {worker_id}")
    worker = get_object_or_404(Workers, pk=worker_id)
    logger.info(f"Изменяемый сотрудник: {worker.last_name} {worker.first_name}, ID-{worker.worker_id}")
    if request.method == 'POST':
        form = ChangeUser(request.POST, instance=worker)
        if form.is_valid():
            form.save()
            logger.info(f"Изменения сохранены администратором:")
            return HttpResponseRedirect(reverse('show_users'))
    else:
        form = ChangeUser(instance=worker)
    context = {'user': worker, 'change_user_form': form}
    return render(request, 'users/change_user.html', context)



def show_delete_user(request, worker_id):
    '''Отобрадение пользователя для удаления'''
    worker = Workers.objects.get(pk=worker_id)
    context = {'worker': worker}
    return render(request, 'users/delete_user.html', context)


def delete_user(request , worker_id):
    '''Удаление пользователя'''
    worker = get_object_or_404(Workers, pk=worker_id)
    worker.delete()
    return HttpResponseRedirect(reverse('show_users'))

def register(request):
    '''Регистрация нового пользователя'''
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect(reverse('show_users'))
    else:
        form = CustomUserCreationForm()
    context = {'register_form': form}
    return render(request, 'users/Register.html', context)

def logout(request):
    '''Выход из аккаунта пользователя'''
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))