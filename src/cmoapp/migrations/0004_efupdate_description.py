# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-15 09:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmoapp', '0003_auto_20171015_1303'),
    ]

    operations = [
        migrations.AddField(
            model_name='efupdate',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]