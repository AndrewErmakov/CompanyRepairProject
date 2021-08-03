from django.contrib.auth.models import User
from django.db import models


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Данные клиента')
    address = models.CharField(max_length=100, verbose_name='Адрес')
    phone_number = models.CharField(max_length=17, verbose_name='Номер телефона для связи')
    is_worker = models.BooleanField(verbose_name='Является сотрудником?', default=False)

    def __str__(self):
        return self.user.username + ' id:' + str(self.user.pk)
