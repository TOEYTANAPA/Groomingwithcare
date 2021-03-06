# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-04-29 06:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('email', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=1000)),
                ('password1', models.CharField(max_length=200)),
                ('password2', models.CharField(max_length=200)),
                ('pic', models.ImageField(default='', upload_to='images/')),
                ('mobilephone', models.CharField(max_length=200)),
            ],
        ),
    ]
