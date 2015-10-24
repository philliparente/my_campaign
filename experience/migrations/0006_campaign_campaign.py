# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('experience', '0005_session_characters'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='campaign',
            field=models.ForeignKey(related_name='master', default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
