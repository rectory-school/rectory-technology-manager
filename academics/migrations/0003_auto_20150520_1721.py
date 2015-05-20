# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0002_auto_20150520_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentpermrec',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='studentpermrec',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='studentpermrec',
            name='nickname',
            field=models.CharField(max_length=50, blank=True),
        ),
    ]
