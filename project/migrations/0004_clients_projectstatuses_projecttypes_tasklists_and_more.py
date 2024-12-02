# Generated by Django 5.1.1 on 2024-10-31 06:03

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_alter_project_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('client_id', models.AutoField(primary_key=True, serialize=False)),
                ('client_surname', models.CharField(max_length=50)),
                ('client_name', models.CharField(max_length=50)),
                ('client_father_name', models.CharField(blank=True, max_length=50, null=True)),
                ('client_email', models.EmailField(max_length=50, unique=True)),
                ('client_phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='RU', unique=True)),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
                'db_table': 'clients',
                'ordering': ['client_surname'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProjectStatuses',
            fields=[
                ('status_id', models.AutoField(primary_key=True, serialize=False)),
                ('status_name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Project Status',
                'verbose_name_plural': 'Project Statuses',
                'db_table': 'project_statuses',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProjectTypes',
            fields=[
                ('type_id', models.AutoField(primary_key=True, serialize=False)),
                ('type_name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Project Type',
                'verbose_name_plural': 'Project Types',
                'db_table': 'project_types',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TaskLists',
            fields=[
                ('list_id', models.AutoField(primary_key=True, serialize=False)),
                ('list_name', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Task List',
                'verbose_name_plural': 'Task Lists',
                'db_table': 'task_lists',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TaskStatuses',
            fields=[
                ('status_id', models.AutoField(primary_key=True, serialize=False)),
                ('status_name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Task Status',
                'verbose_name_plural': 'Task Statuses',
                'db_table': 'task_statuses',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]