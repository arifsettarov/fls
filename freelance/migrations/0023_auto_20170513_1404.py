# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-13 11:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freelance', '0022_auto_20170513_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='mailed',
            field=models.NullBooleanField(default=0),
        ),
    ]
