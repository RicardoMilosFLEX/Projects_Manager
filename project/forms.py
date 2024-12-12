from cProfile import label

from django import forms

from project.models import Projects, Tasks

class ProjectForm(forms.ModelForm):
    """Форма для создания новых проектов"""
    plan_start_date = forms.DateField(label='Дата старта проекта',
                                      widget=forms.DateInput(
                                          attrs={'type':'date',
                                                 'class': 'datepicker'}
                                      ))
    plan_finish_date = forms.DateField(label='Планируемая дата окончания проекта',
                                       widget=forms.DateInput(
        attrs={'type': 'date', 'class': 'datepicker'}
    ))

    class Meta:
        model = Projects
        fields = ('project_name', 'description','status',
                  'responsible','plan_start_date','plan_finish_date','client',
                  'type',)
        labels = {
            'project_name': 'Название проекта',
            'description': 'Описание проекта',
            'status': 'Статус проекта',
            'responsible': 'Ответственный за проект',
            'client': 'Клиент',
            'type':'Тип проекта',
        }

class TaskForm(forms.ModelForm):
    '''Форма создания задач'''
    start_date = forms.DateField(widget=forms.DateInput(
        attrs={'type': 'date', 'class': 'datepicker'}
    ))
    plan_finish_date = forms.DateField(widget=forms.DateInput(
        attrs={'type': 'date', 'class': 'datepicker'}
    ))
    class Meta:
        model = Tasks
        fields = ('description','start_date',
                  'plan_finish_date','list','status','priority')
        labels = {
            'description':'Описание',
            'start_date':'Дата начала задачи',
            'plan_finish_date': 'Дата окончания',
            'list':'Список задач',
            'status':'Статус',
            'priority':'Приоритет',
        }