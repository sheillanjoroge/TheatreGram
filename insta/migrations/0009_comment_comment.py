# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-15 16:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0008_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment',
            field=models.CharField(max_length=250),
            preserve_default=False,
        ),
    ]
