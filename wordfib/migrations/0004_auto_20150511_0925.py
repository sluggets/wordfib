# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wordfib', '0003_auto_20150506_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fakedefinitions',
            name='definition',
            field=models.CharField(max_length=700),
        ),
        migrations.AlterField(
            model_name='fakedefinitions',
            name='fake_definition',
            field=models.CharField(null=True, blank=True, max_length=700),
        ),
        migrations.AlterField(
            model_name='wordandtrue',
            name='definition',
            field=models.CharField(max_length=700),
        ),
        migrations.AlterField(
            model_name='wordandtrue',
            name='real_definition',
            field=models.CharField(null=True, blank=True, max_length=700),
        ),
    ]
