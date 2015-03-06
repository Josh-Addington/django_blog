# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogging', '0006_auto_20150303_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='project',
            field=models.CharField(max_length=250, blank=True),
            preserve_default=True,
        ),
    ]
