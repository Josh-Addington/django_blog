# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_project_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='preview',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]
