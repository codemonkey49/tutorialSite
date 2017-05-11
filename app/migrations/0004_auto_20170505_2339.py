# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-05 23:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_componentmodel_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='componentmodel',
            name='id',
        ),
        migrations.AddField(
            model_name='componentmodel',
            name='compID',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]