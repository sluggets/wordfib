# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wordfib', '0002_correctguess'),
    ]

    operations = [
        migrations.AddField(
            model_name='fakedefinitions',
            name='definition',
            field=models.CharField(blank=True, null=True, max_length=700),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='wordandtrue',
            name='definition',
            field=models.CharField(blank=True, null=True, max_length=700),
            preserve_default=True,
        ),
    ]
