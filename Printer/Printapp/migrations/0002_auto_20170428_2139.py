# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Printapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model_project',
            name='model_price',
            field=models.IntegerField(max_length=2),
        ),
    ]
