# Generated by Django 5.1.1 on 2024-11-03 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_priorities_tasks'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('project_id', models.AutoField(primary_key=True, serialize=False)),
                ('project_name', models.CharField(max_length=50)),
                ('project_description', models.TextField()),
                ('plan_start_date', models.DateField()),
                ('plan_end_date', models.DateField()),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
                'db_table': 'projects',
                'managed': False,
            },
        ),
    ]