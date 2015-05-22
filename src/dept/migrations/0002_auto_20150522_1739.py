# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dept', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='courses',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('s_no', models.IntegerField()),
                ('course_id', models.CharField(max_length=30)),
                ('course_name', models.CharField(max_length=30)),
                ('degree', models.CharField(max_length=30)),
                ('year', models.IntegerField()),
                ('sem', models.IntegerField()),
                ('credits', models.IntegerField()),
                ('course_of_dept', models.CharField(max_length=30)),
                ('course_in_dept', models.CharField(max_length=30)),
                ('type', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='faculty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, null=True, blank=True)),
                ('dept', models.CharField(max_length=50, null=True, blank=True)),
                ('designation', models.CharField(max_length=20, null=True, blank=True)),
                ('qualification', models.CharField(max_length=100, null=True, blank=True)),
                ('area_of_interest', models.CharField(max_length=100, null=True, blank=True)),
                ('contact', models.CharField(max_length=50, null=True, blank=True)),
                ('email', models.EmailField(max_length=254)),
                ('status', models.CharField(max_length=10, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='gallery',
            fields=[
                ('gallery_id', models.CharField(max_length=30, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='notifications',
            fields=[
                ('notif_id', models.CharField(max_length=30, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='staff',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('dept', models.CharField(max_length=50)),
                ('designation', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('roll_no', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('course_enrolled', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.RemoveField(
            model_name='department',
            name='id',
        ),
        migrations.AlterField(
            model_name='department',
            name='dept_code',
            field=models.CharField(max_length=10, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='dept_info',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='department',
            name='dept_name',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
