# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Printapp', '0003_auto_20170428_2140'),
    ]

    operations = [
        migrations.AddField(
            model_name='stlfile',
            name='model_image',
            field=models.ImageField(default=b'/stl_file/stl_image', upload_to=b'/stl_file/stl_image'),
        ),
    ]
