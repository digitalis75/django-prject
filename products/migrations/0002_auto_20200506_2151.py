# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-05-06 21:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='product',
            unique_together=set([('name', 'slug')]),
        ),
    ]
