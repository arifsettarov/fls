# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-28 10:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freelance', '0026_auto_20170528_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokraska',
            name='money',
            field=models.CharField(max_length=100),
        ),
    ]
