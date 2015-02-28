# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogging', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='project',
            field=models.CharField(blank=True, max_length=200),
            preserve_default=True,
        ),
    ]
