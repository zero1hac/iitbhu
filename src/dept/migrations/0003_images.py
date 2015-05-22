# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dept', '0002_auto_20150522_1739'),
    ]

    operations = [
        migrations.CreateModel(
            name='images',
            fields=[
                ('image_id', models.CharField(max_length=30, serialize=False, primary_key=True)),
                ('gallery_id', models.CharField(max_length=30)),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('link', models.URLField()),
                ('caption', models.CharField(max_length=30, null=True, blank=True)),
            ],
        ),
    ]
