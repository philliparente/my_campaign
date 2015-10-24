# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('experience', '0006_campaign_campaign'),
    ]

    operations = [
        migrations.RenameField(
            model_name='campaign',
            old_name='campaign',
            new_name='author',
        ),
    ]
