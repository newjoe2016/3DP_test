# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Printapp', '0005_auto_20170503_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stlfile',
            name='stl_image',
            field=models.ImageField(default=b'stl_file/stl_image', upload_to=b'stl_file/stl_image'),
        ),
    ]
