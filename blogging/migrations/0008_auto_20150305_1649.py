# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogging', '0007_auto_20150305_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='project',
            field=models.ForeignKey(to='projects.Project'),
            preserve_default=True,
        ),
    ]
