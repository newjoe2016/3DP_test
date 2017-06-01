# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Model_project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('model_name', models.CharField(max_length=20)),
                ('model_owner', models.CharField(max_length=20)),
                ('model_price', models.IntegerField()),
                ('model_introd', models.TextField()),
                ('model_image', models.ImageField(default=b'model/model_image', upload_to=b'model/model_image')),
                ('model_file', models.FileField(default=b'model/model_file', upload_to=b'model/model_file')),
                ('model_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Printer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Printer_name', models.CharField(default=b'name', max_length=20)),
                ('max_x', models.IntegerField()),
                ('max_y', models.IntegerField()),
                ('max_z', models.IntegerField()),
                ('nozzle_nr', models.IntegerField(default=1)),
                ('layer_height', models.DecimalField(default=0.2, max_digits=3, decimal_places=2)),
                ('shell_thick', models.DecimalField(default=0.8, max_digits=3, decimal_places=2)),
                ('Infill', models.IntegerField(default=20)),
                ('Print_Speed', models.IntegerField(default=60)),
                ('nozzle_temperature', models.IntegerField(default=220)),
                ('bed_temperature', models.IntegerField(default=60)),
                ('Support_Angle', models.IntegerField(default=60)),
                ('Retract_Length', models.DecimalField(default=5, max_digits=3, decimal_places=2)),
                ('Retract_Speed', models.DecimalField(default=25, max_digits=4, decimal_places=2)),
                ('support_range', models.CharField(default=b'everywhere', max_length=20)),
                ('Plate_Type', models.CharField(default=b'Brim', max_length=20)),
                ('pr_type', models.CharField(max_length=20)),
                ('filament', models.CharField(default=b'PLA', max_length=20)),
                ('owner', models.CharField(max_length=20)),
                ('pr_state', models.IntegerField(default=0)),
                ('pr_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='StlFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stl_file', models.FileField(default=b'stl_file', upload_to=b'stl_file')),
                ('stl_owner', models.CharField(max_length=20)),
                ('stl_name', models.CharField(max_length=20)),
                ('stl_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('money', models.IntegerField(default=0)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
