# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dept', '0003_images'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='courses',
            new_name='course',
        ),
        migrations.RenameModel(
            old_name='images',
            new_name='image',
        ),
        migrations.RenameModel(
            old_name='notifications',
            new_name='notification',
        ),
    ]
