# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-12 10:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_auto_20170612_1122'),
    ]

    operations = [
        migrations.AddField(
            model_name='language',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='language',
            name='description_es',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='language',
            name='description_fr',
            field=models.TextField(null=True),
        ),
    ]