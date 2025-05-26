
from django.contrib.auth.forms import AuthenticationForm
from django import forms

from users.models import Workers

class CustomUserCreationForm(forms.ModelForm):
    '''Форма для создания пользователя'''
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput)

    class Meta:
        model = Workers
        fields = ('last_name', 'first_name', 'father_name', 'email','phone', 'position','password')
        labels = {
            'last_name': 'Фамилия',
            'first_name': 'Имя',
            'father_name': 'Отчество',
            'position': 'Должность',
            'phone': 'Телефон',
        }

    def clean_password2(self):
        '''Метод проверки на совпадение паролей'''
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        '''Метод сохрания пользователя'''
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class EmailAuthenticationForm(AuthenticationForm):
    '''Форма авторизации пользователя'''
    username = forms.EmailField(label='Email', widget=forms.EmailInput)
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)

    class Meta:
        model = Workers
        fields = ('username','password')

class ChangeUser(forms.ModelForm):
    '''Форма изменения пользователя'''
    class Meta:
        model = Workers
        fields = ('last_name', 'first_name',
                  'father_name', 'email','phone','work_phone',
                  )
        labels = {
            'last_name': 'Фамилия',
            'first_name': 'Имя',
            'father_name': 'Отчество',
            'email': "Почта",
            'phone': 'Телефон',
            'work_phone': 'Рабочий телефон',
        }

class ChangeUserPositionForm(forms.ModelForm):
    
    class Meta: 
        model = Workers
        fields = ('position',)
        labels = {
            'position' : 'Должность'
        }


