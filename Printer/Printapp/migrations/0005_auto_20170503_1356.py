# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Printapp', '0004_stlfile_model_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stlfile',
            old_name='model_image',
            new_name='stl_image',
        ),
    ]
