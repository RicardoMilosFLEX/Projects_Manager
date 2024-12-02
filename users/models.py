from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User, AbstractUser
from django.db import models
from django.db.models import Model
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

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
    task = models.ForeignKey('project.Tasks', on_delete=models.CASCADE, related_name='tasks')

    class Meta:
        db_table = 'workers_groups'
        managed = False
        verbose_name = 'workers group'
        verbose_name_plural = 'workers groups'
    #
    # def __str__(self):
    #     return self.group_id

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class Workers(AbstractUser):
    '''Модель работника'''
    worker_id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
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
    password = models.CharField(max_length=500)
    date_joined = models.DateTimeField('date joined', auto_now_add=True)


    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    def __str__(self):
          return self.email

    class Meta:
        db_table = 'workers'
        managed = False
        verbose_name = 'worker'
        verbose_name_plural = 'workers'

    @property
    def last_login(self):
        return None  # Или возвращайте фиктивное значение

    @property
    def get_username(self):
        return None  # Или возвращайте фиктивное значение

    @property
    def is_superuser(self):
        return False  # Настройте по необходимости

    @property
    def username(self):
        return self.email  # Возвращаем email вместо username

    @property
    def is_active(self):
        return True

    def date_joined(self):
        return timezone.now()

    @property
    def is_staff(self):
        return False
    def has_perm(self, perm, obj=None):
        return True  # Настройте на основе логики вашего приложения

    def has_module_perms(self, app_label):
        return True

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



# class Users(models.Model):
#     user = models.OneToOneField(Workers,
#                                    on_delete=models.CASCADE,
#                                    related_name='user',
#                                    primary_key=True)
#     email = models.EmailField(max_length=50,
#                               unique=True)
#     password = models.CharField(max_length=50)
#     position = models.ForeignKey(ListPositions,
#                                     on_delete=models.CASCADE,
#                                     related_name='users_position',
#                                     to_field='position_id')
#
#     def __str__(self):
#         return self.email
#
#     class Meta:
#         db_table = 'users'
#         managed = False
#         verbose_name = 'user'
#         verbose_name_plural = 'users'