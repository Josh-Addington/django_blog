# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_project_js'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='code',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='js',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
    ]
