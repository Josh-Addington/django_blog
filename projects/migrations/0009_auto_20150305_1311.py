# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_auto_20150304_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='preview',
            field=models.CharField(default='', max_length=250),
            preserve_default=False,
        ),
    ]
