# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-08 12:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freelance', '0045_delete_workers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('telephone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('SNILS', models.IntegerField(verbose_name='СНИЛС')),
                ('password', models.CharField(max_length=100, verbose_name='Пароль')),
                ('type', models.TextField(default='')),
                ('region', models.CharField(default='', max_length=200)),
            ],
            options={
                'verbose_name': 'Соискатели',
                'db_table': 'Workers',
            },
        ),
    ]
