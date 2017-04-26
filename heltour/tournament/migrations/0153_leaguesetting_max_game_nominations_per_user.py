# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-04-03 16:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0152_leaguesetting'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaguesetting',
            name='max_game_nominations_per_user',
            field=models.PositiveIntegerField(default=3),
        ),
    ]