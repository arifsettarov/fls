# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-29 11:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freelance', '0036_krovlya'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poli',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ploshad', models.CharField(max_length=20)),
                ('type_pokr', models.CharField(max_length=20)),
                ('works', models.TextField()),
                ('details', models.TextField()),
                ('money', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=20)),
                ('district', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField(default=None)),
                ('mailed', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'poli',
                'verbose_name': 'Полы',
            },
        ),
    ]
