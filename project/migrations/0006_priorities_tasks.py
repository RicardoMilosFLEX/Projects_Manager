# Generated by Django 5.1.1 on 2024-11-03 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_alter_clients_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Priorities',
            fields=[
                ('priority_id', models.AutoField(primary_key=True, serialize=False)),
                ('priority_name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Priority',
                'verbose_name_plural': 'Priorities',
                'db_table': 'priorities',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('task_id', models.AutoField(primary_key=True, serialize=False)),
                ('start_date', models.DateField()),
                ('plan_finish_date', models.DateField()),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Task',
                'verbose_name_plural': 'Tasks',
                'db_table': 'tasks',
                'managed': False,
            },
        ),
    ]
