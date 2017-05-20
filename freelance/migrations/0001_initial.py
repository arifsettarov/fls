# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-12 15:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Type_of_Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Обл. деятельности',
            },
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('type', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='freelance.Type_of_Work')),
            ],
            options={
                'verbose_name': 'Под-обл. деятельности',
            },
        ),
    ]