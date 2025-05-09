from django.contrib.auth.models import  AbstractUser
from django.db import models
from django.db.models import  CharField
from django.utils import timezone
from django.contrib.auth.models import  BaseUserManager

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
class CustomUserManager(BaseUserManager):
    '''Класс для управления моделью пользователя'''

    def create_user(self, email, password=None, **extra_fields):
        '''Логика создания нового пользователя'''
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        '''Логика создания суперпользователя'''
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)


class Workers(AbstractUser):
    '''Модель работника'''
    worker_id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50 , blank=True, null=True)
    email = models.EmailField(max_length=50, unique=True)
    phone = CharField(max_length=50, blank=True, null=True)
    work_phone = models.CharField(max_length=6, unique=True, blank=True, null=True)
    position = models.ForeignKey(ListPositions,
                                    on_delete=models.PROTECT,
                                    related_name='position',
                                    to_field='position_id')
    password = models.CharField(max_length=500)



    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name','phone','position','password',]
    def __str__(self):
          return f'{self.first_name} {self.last_name}'

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

    def get_username(self):
        return self.email

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

