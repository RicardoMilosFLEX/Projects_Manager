# Generated by Django 5.1.1 on 2024-10-14 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['name'], 'verbose_name': 'Проект', 'verbose_name_plural': 'Проекты'},
        ),
        migrations.AddField(
            model_name='project',
            name='end_date',
            field=models.DateField(null=True, verbose_name='Плановая дата окончания'),
        ),
        migrations.AddField(
            model_name='project',
            name='manager',
            field=models.CharField(default='w', max_length=30, verbose_name='Менеджер проекта'),
        ),
        migrations.AddField(
            model_name='project',
            name='project_client',
            field=models.CharField(default='w', max_length=20, verbose_name='Клиент'),
        ),
        migrations.AddField(
            model_name='project',
            name='project_type',
            field=models.CharField(default=None, max_length=20, verbose_name='Тип проекта'),
        ),
        migrations.AddField(
            model_name='project',
            name='start_date',
            field=models.DateField(null=True, verbose_name='Плановая дата старта проекта'),
        ),
        migrations.AddField(
            model_name='project',
            name='task_list',
            field=models.CharField(default=None, max_length=20, verbose_name='Список задач'),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(max_length=20, verbose_name='Статус'),
        ),
    ]
