# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogging', '0008_auto_20150305_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='project',
            field=models.ManyToManyField(to='projects.Project'),
            preserve_default=True,
        ),
    ]
