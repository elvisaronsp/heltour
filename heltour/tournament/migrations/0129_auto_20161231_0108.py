# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-31 01:08
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0128_auto_20161230_2204'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlternatesManagerSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('contact_interval', models.DurationField(default=datetime.timedelta(0, 28800), help_text='How long before the next alternate will be contacted during the round.')),
                ('unresponsive_interval', models.DurationField(default=datetime.timedelta(1), help_text='How long after being contacted until an alternate will be marked as unresponsive.')),
                ('contact_before_round_start', models.BooleanField(default=True, help_text='If we should search for alternates before the pairings are published. Has no effect for round 1.')),
                ('contact_offset_before_round_start', models.DurationField(default=datetime.timedelta(2), help_text='How long before the round starts we should start searching for alternates. Also ends the previous round searches early.')),
                ('contact_interval_before_round_start', models.DurationField(default=datetime.timedelta(0, 43200), help_text="How long before the next alternate will be contacted, if the round hasn't started yet.")),
                ('league', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tournament.League')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='season',
            name='enable_alternates_manager',
        ),
    ]
