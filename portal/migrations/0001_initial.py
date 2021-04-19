# Generated by Django 3.2 on 2021-04-19 08:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=400, null=True, verbose_name='Наименование')),
                ('topic', models.CharField(blank=True, max_length=500, null=True, verbose_name='Тема')),
                ('ip', models.GenericIPAddressField(blank=True, null=True, verbose_name='Айпи адрес')),
                ('floor', models.IntegerField(blank=True, null=True, verbose_name='Этаж')),
                ('office', models.IntegerField(blank=True, null=True, verbose_name='Кабинет')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('state', models.CharField(blank=True, choices=[('Не зарегистрировано', 'Не зарегистрированно'), ('Зарегистрировано', 'Зарегистрировано'), ('Выполнено', 'Выполнено')], max_length=256, null=True, verbose_name='Состояние')),
                ('service', models.CharField(blank=True, choices=[('ИТ', 'ИТ'), ('АХО', 'АХО')], max_length=256, null=True, verbose_name='Услуга')),
                ('service_detail', models.CharField(blank=True, choices=[], max_length=256, null=True, verbose_name='Состав услуги')),
                ('date_of_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_of_closed', models.DateTimeField(blank=True, null=True, verbose_name='Дата закрытия')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
    ]
