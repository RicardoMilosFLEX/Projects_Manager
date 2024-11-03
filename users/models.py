from django.db import models
from django.db.models import Model

from project.models import Tasks
from phonenumber_field.modelfields import PhoneNumberField

class ListPositions(models.Model):
    '''Список должностей'''
    position_id = models.AutoField(primary_key=True)
    position_name = models.CharField(max_length=50)

    class Meta:
        db_table = 'list_position'
        managed = False
        verbose_name = 'list_position'
        verbose_name_plural = 'list_positions'

    def __str__(self):
        return self.position_name

# не особо корректно работает (Может и не надо это)
class WorkersGroups(models.Model):
    '''Модель групп сотрудников'''
    group_id = models.AutoField(primary_key=True)
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE, related_name='tasks')

    class Meta:
        db_table = 'workers_groups'
        managed = False
        verbose_name = 'workers group'
        verbose_name_plural = 'workers groups'
    #
    # def __str__(self):
    #     return self.group_id

class Workers(models.Model):
    '''Модель работника'''
    worker_id = models.AutoField(primary_key=True)
    surname = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50 , blank=True, null=True)
    email = models.EmailField(max_length=50, unique=True)
    phone = PhoneNumberField(region='RU', unique=True)
    work_phone = models.CharField(max_length=6, unique=True, blank=True, null=True)
    position = models.ForeignKey(ListPositions,
                                    on_delete=models.CASCADE,
                                    related_name='position',
                                    to_field='position_id')
    group_name = models.ForeignKey(WorkersGroups, on_delete=models.CASCADE,
                                   related_name='group', blank=True, null=True)

    def __str__(self):
          return self.email

    class Meta:
        db_table = 'workers'
        managed = False
        verbose_name = 'worker'
        verbose_name_plural = 'workers'


class Responsible(models.Model):
    '''Модель ответственного'''
    responsible = models.OneToOneField(Workers, on_delete=models.CASCADE, related_name='responsible', primary_key=True)
    surname = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50 , blank=True, null=True)
    email = models.EmailField(max_length=50, unique=True)
    phone = PhoneNumberField(region='RU', unique=True)

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'responsible'
        managed = False
        verbose_name = 'responsible'
        verbose_name_plural = 'responsible'





