# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogging', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='project',
            field=models.ManyToManyField(to='projects.Project', null=True),
            preserve_default=True,
        ),
    ]
