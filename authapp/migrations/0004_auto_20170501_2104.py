# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-05-01 14:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0003_dog_picdog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='picDog',
            field=models.FileField(default='', upload_to='documents/'),
        ),
    ]
