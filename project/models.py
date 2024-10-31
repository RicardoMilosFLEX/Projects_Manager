from phonenumber_field.modelfields import PhoneNumberField
from django.db import models

class Clients(models.Model):
    '''Модель клиентов'''
    client_id = models.AutoField(primary_key=True)
    surname = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=50, unique=True)
    phone = PhoneNumberField(unique=True, region='RU')

    def __str__(self):
        return self.surname

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
    '''Модлеь статусов задач'''
    status_id = models.AutoField(primary_key=True)
    status_name = models.CharField(max_length=50)

    class Meta:
        db_table = 'task_statuses'
        verbose_name = 'Task Status'
        verbose_name_plural = 'Task Statuses'
        managed = False

    def __str__(self):
        return self.status_name
