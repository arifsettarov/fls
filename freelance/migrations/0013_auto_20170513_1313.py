# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-13 10:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('freelance', '0012_auto_20170513_1250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workers',
            name='SNILS',
        ),
        migrations.RemoveField(
            model_name='workers',
            name='email',
        ),
        migrations.RemoveField(
            model_name='workers',
            name='name',
        ),
        migrations.RemoveField(
            model_name='workers',
            name='password',
        ),
        migrations.RemoveField(
            model_name='workers',
            name='region',
        ),
        migrations.RemoveField(
            model_name='workers',
            name='telephone',
        ),
        migrations.RemoveField(
            model_name='workers',
            name='type',
        ),
    ]
