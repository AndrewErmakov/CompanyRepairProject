from django.contrib.auth.models import User
from django.db import models
from clients_app.models import Client


class Request(models.Model):
    REQUESTS_TYPE_CHOICES = [
        ('Ремонт', 'Ремонт'),
        ('Обслуживание', 'Обслуживание'),
        ('Консультация', 'Консультация'),
    ]

    STATUS_CHOICES = [
        ('Открыта', 'Открыта'),
        ('В работе', 'В работе'),
        ('Закрыта', 'Закрыта'),
    ]

    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    type = models.CharField(verbose_name='Тип заявки', choices=REQUESTS_TYPE_CHOICES, max_length=30)
    status = models.CharField(verbose_name='Статус заявки', choices=STATUS_CHOICES, max_length=20)
    customer = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Клиент')
    executor = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Исполнитель', blank=True,
                                 null=True)

