# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-28 09:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freelance', '0024_link_section'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Uteplenie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ploshad', models.CharField(max_length=25)),
                ('rooms', models.CharField(max_length=15)),
                ('material_ot', models.CharField(max_length=20)),
                ('details', models.TextField()),
                ('money', models.IntegerField(default=0)),
                ('city', models.CharField(max_length=20)),
                ('district', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'db_table': 'uteplenie',
                'verbose_name': 'Утепление фасадов',
            },
        ),
        migrations.RemoveField(
            model_name='orders',
            name='region',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='type',
        ),
        migrations.AlterModelOptions(
            name='link_section',
            options={'verbose_name': 'Иконки разделов'},
        ),
        migrations.DeleteModel(
            name='Orders',
        ),
    ]
