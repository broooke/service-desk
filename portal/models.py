from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Service(models.Model):
    name = models.CharField('Услуга', max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name


class ServiceDetail(models.Model):
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, verbose_name='Услуга', blank=True, null=True)
    name = models.CharField('Состав услуги', max_length=400, null=True, blank=True)

    def __str__(self):
        return self.name


class Application(models.Model):
    STATE_CHOICES = [
        ('Не зарегистрировано', 'Не зарегистрированно'),
        ('Зарегистрировано', 'Зарегистрировано'),
        ('Выполнено', 'Выполнено'),
    ]

    topic = models.CharField('Тема', max_length=500, null=True, blank=True)
    user = models.CharField('Пользователь', max_length=500, null=True, blank=True)
    ip = models.GenericIPAddressField('Айпи адрес', null=True, blank=True)
    floor = models.IntegerField('Этаж', null=True, blank=True)
    office = models.IntegerField('Кабинет', null=True, blank=True)
    text = models.TextField('Описание', null=True, blank=True)
    state = models.CharField('Состояние', max_length=256, choices=STATE_CHOICES, null=True, blank=True)
    service = models.ForeignKey(Service, verbose_name='Услуга', on_delete=models.SET_NULL, null=True, blank=True)
    service_detail = models.ForeignKey(ServiceDetail, verbose_name='Состав услуги', on_delete=models.SET_NULL, null=True, blank=True)
    date_of_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return "Обращение №" + str(self.id)
