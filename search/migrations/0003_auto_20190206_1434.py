# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-02-06 14:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_auto_20190206_1432'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='company',
            new_name='company_id',
        ),
    ]
