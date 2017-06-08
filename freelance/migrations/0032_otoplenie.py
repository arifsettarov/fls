# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-29 08:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freelance', '0031_auto_20170528_1530'),
    ]

    operations = [
        migrations.CreateModel(
            name='Otoplenie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_type', models.CharField(max_length=20)),
                ('ploshad', models.CharField(max_length=20)),
                ('works', models.CharField(max_length=250)),
                ('kotyol', models.CharField(max_length=50)),
                ('details', models.TextField()),
                ('money', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=20)),
                ('district', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField(default=None)),
                ('mailed', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Отопление',
                'db_table': 'otoplenie',
            },
        ),
    ]
