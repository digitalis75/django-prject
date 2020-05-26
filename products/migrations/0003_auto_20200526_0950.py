# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-05-26 09:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200506_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cover_format',
            field=models.CharField(choices=[('Softback', 'Softback'), ('Hardback', 'Hardback')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='school_level',
            field=models.CharField(choices=[('Primary', 'Primary'), ('Secondary', 'Secondary')], default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='product',
            name='stage',
            field=models.CharField(choices=[('Junior_Infants', 'Junior Infants'), ('Senior_Infants', 'Senior Infants'), ('First_Class', 'First Class'), ('Second_Class', 'Second Class'), ('Third_Class', 'Third Class'), ('Fourth_Class', 'Fourth Class'), ('Fifth_Class', 'Fifth Class'), ('Sixth_Class', 'Sixth Class')], default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='product',
            name='subject',
            field=models.CharField(choices=[('English', 'English'), ('Irish', 'Irish'), ('Maths', 'Maths'), ('Science', 'Science'), ('SESE', 'SESE'), ('Science/SESE', 'Science/SESE'), ('Geograghy', 'Geograghy'), ('History', 'History')], default='', max_length=40),
        ),
    ]
