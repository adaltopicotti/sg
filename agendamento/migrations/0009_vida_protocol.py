# Generated by Django 2.0.3 on 2018-04-22 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agendamento', '0008_auto_20180421_2156'),
    ]

    operations = [
        migrations.AddField(
            model_name='vida',
            name='protocol',
            field=models.TextField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
