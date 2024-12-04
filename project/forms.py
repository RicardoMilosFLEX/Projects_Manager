from django import forms

from project.models import Projects


class ProjectForm(forms.ModelForm):
    """Форма для создания новых проектов"""
    plan_start_date = forms.DateField(label='Дата старта проекта', widget=forms.DateInput(attrs={'type':'date',
                                                                                            'class': 'datepicker'}))
    plan_finish_date = forms.DateField(label='Планируемая дата окончания проекта', widget=forms.DateInput(
        attrs={'type': 'date', 'class': 'datepicker'}))

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
