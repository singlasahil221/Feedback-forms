# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-05 11:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('former', '0029_auto_20180105_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='forms',
            name='description',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='question',
            name='forms',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='former.Forms'),
        ),
    ]
