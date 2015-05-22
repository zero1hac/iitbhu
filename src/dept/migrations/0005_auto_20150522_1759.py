# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dept', '0004_auto_20150522_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_in_dept',
            field=models.CharField(max_length=100),
        ),
    ]
