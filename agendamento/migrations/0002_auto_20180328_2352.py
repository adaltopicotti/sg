# Generated by Django 2.0.3 on 2018-03-29 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agendamento', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='segurado',
            old_name='cidade',
            new_name='municipio',
        ),
        migrations.AlterField(
            model_name='ramo',
            name='nome',
            field=models.CharField(choices=[('Empresarial', 'Empresarial'), ('Vida', 'Vida'), ('Frota', 'Frota')], max_length=20),
        ),
    ]