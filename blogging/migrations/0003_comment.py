# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogging', '0002_auto_20150225_1819'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('author', models.CharField(max_length=25)),
                ('text', models.TextField()),
                ('posted_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('post', models.ForeignKey(to='blogging.Post')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
