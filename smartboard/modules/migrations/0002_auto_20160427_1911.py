# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-27 18:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lecture',
            old_name='lecture_code',
            new_name='module_code',
        ),
    ]
