# Generated by Django 2.0.3 on 2018-05-02 15:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('agendamento', '0015_auto_20180426_1240'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgendamentoPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('agendamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agendamento.Agendamento')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
