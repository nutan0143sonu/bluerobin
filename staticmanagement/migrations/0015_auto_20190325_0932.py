# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-25 09:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staticmanagement', '0014_auto_20190325_0739'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='howitworks',
            options={'ordering': ('-id',), 'verbose_name': 'How it Works?', 'verbose_name_plural': 'How it Works?'},
        ),
    ]
