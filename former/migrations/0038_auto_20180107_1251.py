# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-07 07:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('former', '0037_auto_20180107_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='forms',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='former.Forms'),
        ),
    ]
