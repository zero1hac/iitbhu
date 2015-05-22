# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dept', '0005_auto_20150522_1759'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='course_enrolled',
            new_name='batch',
        ),
    ]
