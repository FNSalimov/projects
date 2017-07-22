# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('english', '0003_feed'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Feed',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
