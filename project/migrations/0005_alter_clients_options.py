# Generated by Django 5.1.1 on 2024-10-31 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_clients_projectstatuses_projecttypes_tasklists_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clients',
            options={'managed': False, 'ordering': ['surname'], 'verbose_name': 'Client', 'verbose_name_plural': 'Clients'},
        ),
    ]
