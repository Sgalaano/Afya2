# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-12 10:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctors',
            name='doctype',
            field=models.CharField(choices=[('Pedetritian', 'Family Doctor'), ('Gynecologist', 'Dermatologist'), ('Pyschiatrist', 'Other')], max_length=60),
        ),
    ]