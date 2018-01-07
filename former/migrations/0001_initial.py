# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-07 11:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ans', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Forms',
            fields=[
                ('p_id', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('form_name', models.CharField(default='', max_length=50)),
                ('description', models.CharField(default='', max_length=1000)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='question',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ques', models.CharField(default=' ', max_length=1000)),
                ('qtype', models.CharField(default=0, max_length=1)),
                ('forms', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='former.Forms')),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='former.question'),
        ),
    ]
