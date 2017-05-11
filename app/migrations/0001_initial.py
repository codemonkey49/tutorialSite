# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-04 21:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='componentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('componentType', models.CharField(max_length=100)),
                ('componentContent', models.CharField(blank=True, max_length=10000, null=True)),
                ('image', models.CharField(blank=True, max_length=500, null=True)),
                ('imageCaption', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='tutorialModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('component', models.ManyToManyField(to='app.componentModel')),
            ],
        ),
    ]