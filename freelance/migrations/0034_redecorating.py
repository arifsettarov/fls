# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-29 10:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freelance', '0033_osteklenie_balkonov'),
    ]

    operations = [
        migrations.CreateModel(
            name='Redecorating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ploshad', models.CharField(max_length=20)),
                ('rooms', models.CharField(max_length=50)),
                ('works', models.TextField()),
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
                'db_table': 'cosmetic_remont',
                'verbose_name': 'Косметический ремонт',
            },
        ),
    ]