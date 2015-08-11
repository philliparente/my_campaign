# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('character_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('session_title', models.CharField(max_length=200)),
                ('session_date', models.DateTimeField()),
                ('session_characters', models.ForeignKey(to='experience.Character')),
            ],
        ),
    ]
