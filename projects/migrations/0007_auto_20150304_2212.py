# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_project_preview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='preview',
            field=models.ImageField(verbose_name='Project Preview', null=True, blank=True, upload_to='static/images/'),
            preserve_default=True,
        ),
    ]
