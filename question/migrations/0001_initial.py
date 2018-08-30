# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-30 02:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=50, verbose_name='\u95ee\u9898')),
                ('answer', models.CharField(max_length=200, verbose_name='\u56de\u7b54')),
            ],
            options={
                'db_table': 'question',
                'verbose_name': '\u5e38\u89c1\u95ee\u9898',
                'verbose_name_plural': '\u5e38\u89c1\u95ee\u9898',
            },
        ),
    ]
