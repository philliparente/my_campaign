# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('experience', '0003_criteria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='criteria',
            name='value',
            field=models.DecimalField(max_digits=4, decimal_places=0),
        ),
    ]
