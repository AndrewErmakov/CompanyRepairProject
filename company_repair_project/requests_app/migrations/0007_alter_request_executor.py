# Generated by Django 3.2.5 on 2021-08-03 13:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('requests_app', '0006_auto_20210803_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='executor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to=settings.AUTH_USER_MODEL, verbose_name='Исполнитель'),
        ),
    ]