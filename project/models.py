from phonenumber_field.modelfields import PhoneNumberField
from django.db import models

import users.models


class Clients(models.Model):
    '''Модель клиентов'''
    client_id = models.AutoField(primary_key=True)
    surname = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=50, unique=True)
    phone = PhoneNumberField(unique=True, region='RU')



    class Meta:
        db_table = 'clients'
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
        ordering = ['surname']
        managed = False

class ProjectStatuses(models.Model):
    '''Модель статусов проекта'''
    status_id = models.AutoField(primary_key=True)
    status_name = models.CharField(max_length=50)

    class Meta:
        db_table = 'project_statuses'
        verbose_name = 'Project Status'
        verbose_name_plural = 'Project Statuses'
        managed = False

    def __str__(self):
        return self.status_name


class ProjectTypes(models.Model):
    '''Модель типов проектов'''
    type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=50)

    def __str__(self):
        return self.type_name

    class Meta:
        db_table = 'project_types'
        verbose_name = 'Project Type'
        verbose_name_plural = 'Project Types'
        managed = False


class TaskLists(models.Model):
    '''Модель списка задач'''
    list_id = models.AutoField(primary_key=True)
    list_name = models.CharField(max_length=30)

    class Meta:
        db_table = 'task_lists'
        verbose_name = 'Task List'
        verbose_name_plural = 'Task Lists'
        managed = False

    def __str__(self):
        return self.list_name

class TaskStatuses(models.Model):
    '''Модель статусов задач'''
    status_id = models.AutoField(primary_key=True)
    status_name = models.CharField(max_length=50)

    class Meta:
        db_table = 'task_statuses'
        verbose_name = 'Task Status'
        verbose_name_plural = 'Task Statuses'
        managed = False

    def __str__(self):
        return self.status_name


class Priorities(models.Model):
    '''Модель приоритетов'''
    priority_id = models.AutoField(primary_key=True)
    priority_name = models.CharField(max_length=50)

    class Meta:
        db_table = 'priorities'
        verbose_name = 'Priority'
        verbose_name_plural = 'Priorities'
        managed = False

    def __str__(self):
        return self.priority_name

class Tasks(models.Model):
    task_id = models.AutoField(primary_key=True)
    list = models.ForeignKey(TaskLists, on_delete=models.CASCADE, related_name='tasks_lists')
    start_date = models.DateField()
    priority = models.ForeignKey(Priorities, on_delete=models.CASCADE, related_name='tasks_priorities')
    status = models.ForeignKey(TaskStatuses, on_delete=models.CASCADE, related_name='tasks_statuses')
    plan_finish_date = models.DateField()
    description = models.TextField()

    class Meta:
        db_table = 'tasks'
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        managed = False


    def __str__(self):
        return self.description


class Projects(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=50)
    description = models.TextField()
    status = models.ForeignKey(ProjectStatuses,
                               on_delete=models.CASCADE,
                               related_name='project_statuses',
                               to_field='status_id')
    responsible = models.ForeignKey(users.models.Responsible,
                                    on_delete=models.CASCADE,
                                    related_name='project_responsible')
    plan_start_date = models.DateField()
    plan_finish_date = models.DateField()
    client = models.ForeignKey(Clients,
                               on_delete=models.CASCADE,
                               related_name='project_clients')
    type = models.ForeignKey(ProjectTypes,
                             on_delete=models.CASCADE,
                             related_name='project_types')
    tasks_list = models.ForeignKey(TaskLists,
                                  on_delete=models.CASCADE,
                                  related_name='project_task_lists')

    class Meta:
        managed = False
        db_table = 'projects'
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.project_name