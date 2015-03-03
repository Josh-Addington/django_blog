# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogging', '0005_auto_20150303_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='project',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
    ]
