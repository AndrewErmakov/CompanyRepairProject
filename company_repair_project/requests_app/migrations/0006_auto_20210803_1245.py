# Generated by Django 3.2.5 on 2021-08-03 12:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clients_app', '0002_client_is_worker'),
        ('requests_app', '0005_alter_request_executor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to='clients_app.client', verbose_name='Клиент'),
        ),
        migrations.AlterField(
            model_name='request',
            name='executor',
            field=models.ForeignKey(blank=True, default=8, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='tasks', to=settings.AUTH_USER_MODEL, verbose_name='Исполнитель'),
        ),
    ]
