# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('experience', '0004_auto_20150915_1610'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='characters',
            field=models.ManyToManyField(related_name='participating', to='experience.Character'),
        ),
    ]
