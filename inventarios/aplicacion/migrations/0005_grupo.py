# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-22 04:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0004_clasificacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_grupo', models.CharField(max_length=20)),
                ('nombre_subgrupo', models.CharField(max_length=20)),
            ],
        ),
    ]