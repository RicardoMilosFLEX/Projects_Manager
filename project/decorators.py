from django.http import HttpResponseRedirect
from django.urls import reverse
from functools import wraps

def admin_required(view_func):
    """Декоратор для проверки, является ли пользователь администратором.
    Если нет - перенаправляет на главную страницу."""
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated or request.user.position_id != 1:
            return HttpResponseRedirect(reverse('index'))
        return view_func(request, *args, **kwargs)
    return _wrapped_view

def manager_required(view_func):
    """Декоратор для проверки, является ли пользователь менеджером.
    Если нет - перенаправляет на главную страницу."""
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated or request.user.position_id!= 2:
            return HttpResponseRedirect(reverse('index'))
        return view_func(request, *args, **kwargs)
    return _wrapped_view

def worker_required(view_func):
    """Декоратор для проверки, является ли пользователь работником.

    Args:
        view_func (func): Функция представления.
    """
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated or request.user.position_id!= 3:
            return HttpResponseRedirect(reverse('index'))
        return view_func(request, *args, **kwargs)
    return _wrapped_view