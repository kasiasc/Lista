# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-21 20:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplikacja', '0002_auto_20160921_2212'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Page',
            new_name='List',
        ),
    ]