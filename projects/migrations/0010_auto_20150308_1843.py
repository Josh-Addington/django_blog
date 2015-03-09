# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_auto_20150305_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='code',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='js',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='preview',
            field=models.CharField(max_length=250, blank=True),
            preserve_default=True,
        ),
    ]
