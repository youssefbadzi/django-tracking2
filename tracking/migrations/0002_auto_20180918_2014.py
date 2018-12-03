# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('tracking', '0001_initial'),
    ]
    operations = [
        migrations.AlterModelOptions(
            name='visitor',
            options={
                'ordering': ('-start_time',),
                'permissions': (('visitor_log', 'Can view visitor'),)
            },
        ),
    ]
