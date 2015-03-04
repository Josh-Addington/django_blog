# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_project_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='js',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
