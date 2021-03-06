# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import migrations, models
import os

base_dir = os.path.realpath(os.path.dirname(__file__))


def sql_path(filename):
    return os.path.join(base_dir, "sql", filename)


with open(sql_path("in_call.sql")) as file:
    in_call_sql = file.read()

with open(sql_path("officer_activity.sql")) as file:
    officer_activity_sql = file.read()

class Migration(migrations.Migration):
    dependencies = [
        ('officer_allocation', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(in_call_sql),
        migrations.RunSQL(officer_activity_sql)
    ]
