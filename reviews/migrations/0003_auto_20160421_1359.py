# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-21 20:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20160420_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.CharField(choices=[('barf', 'barf'), ('meh', 'meh'), ('aight', 'aight'), ('sick', 'sick'), ('hype-worthy', 'hype-worthy')], max_length=200),
        ),
    ]
