# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dept_code', models.CharField(max_length=10)),
                ('dept_name', models.CharField(max_length=50)),
                ('dept_info', models.CharField(max_length=10000)),
            ],
        ),
    ]
