# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-24 15:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_hotnews'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HotNews',
            new_name='HotNew',
        ),
    ]