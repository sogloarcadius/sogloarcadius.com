# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-13 17:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0007_auto_20170613_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalinfo',
            name='date_of_birth',
            field=models.DateField(),
        ),
    ]