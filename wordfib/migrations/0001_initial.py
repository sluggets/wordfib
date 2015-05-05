# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FakeDefinitions',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('fake_definition', models.CharField(max_length=700)),
                ('votes', models.IntegerField(default=0)),
                ('author', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WordAndTrue',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('word', models.CharField(max_length=50)),
                ('real_definition', models.CharField(max_length=700)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='fakedefinitions',
            name='real_word',
            field=models.ForeignKey(to='wordfib.WordAndTrue'),
            preserve_default=True,
        ),
    ]
