
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth, messages
from django.urls import reverse

from users.forms import EmailAuthenticationForm, CustomUserCreationForm


def login(request):
    if request.method == 'POST':
        form = EmailAuthenticationForm(data=request.POST)
        if form.is_valid():
            email = request.POST['email']
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


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            print(form.errors)
            messages.error(request, form.errors)
    else:
        form = CustomUserCreationForm()
    context = {'register_form': form}
    return render(request, 'users/Register.html', context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))