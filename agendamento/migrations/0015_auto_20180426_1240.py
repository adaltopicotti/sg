# Generated by Django 2.0.3 on 2018-04-26 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agendamento', '0014_auto_20180426_1235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='segurado',
            name='complemento',
        ),
        migrations.RemoveField(
            model_name='segurado',
            name='numero',
        ),
    ]
