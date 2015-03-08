# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogging', '0002_auto_20150307_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='project',
            field=models.ManyToManyField(to='projects.Project', blank=True),
            preserve_default=True,
        ),
    ]
