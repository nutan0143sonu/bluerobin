# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-04 11:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('analyticsmaven', '0048_auto_20180904_0555'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionManagement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipient_share', models.FloatField()),
                ('analytics_share', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaction_job', to='analyticsmaven.AppliedJobs')),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipient', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Transaction Management',
            },
        ),
    ]
