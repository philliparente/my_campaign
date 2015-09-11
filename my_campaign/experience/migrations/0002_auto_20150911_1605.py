# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('experience', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.RenameField(
            model_name='character',
            old_name='character_name',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='session',
            old_name='session_date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='session',
            old_name='session_title',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='session',
            name='session_characters',
        ),
        migrations.AddField(
            model_name='character',
            name='characters',
            field=models.ManyToManyField(related_name='participating', to='experience.Session'),
        ),
        migrations.AddField(
            model_name='character',
            name='name',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='character',
            name='campaign',
            field=models.ForeignKey(default=1, to='experience.Campaign'),
            preserve_default=False,
        ),
    ]
