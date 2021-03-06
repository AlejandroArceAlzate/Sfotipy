# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('tittle', models.CharField(max_length=255)),
                ('order', models.PositiveIntegerField()),
                ('track_file', models.FileField(upload_to='tracks')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
