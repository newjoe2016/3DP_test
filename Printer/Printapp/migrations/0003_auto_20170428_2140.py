# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Printapp', '0002_auto_20170428_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model_project',
            name='model_price',
            field=models.IntegerField(default=20),
        ),
    ]
