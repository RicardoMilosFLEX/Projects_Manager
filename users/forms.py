from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from users.models import Workers

class CustomUserCreationForm(forms.ModelForm):
    '''Форма для создания пользователя'''
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirm', widget=forms.PasswordInput)

    class Meta:
        model = Workers
        fields = ('last_name', 'first_name', 'father_name', 'email', 'position','password')

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
    email = forms.EmailField(label='Email', widget=forms.EmailInput)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    class Meta:
        model = Workers
        fields = ('email','password')
