# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('family_id', models.CharField(unique=True, max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='FamilyMember',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first', models.CharField(max_length=20)),
                ('last', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, blank=True)),
                ('phone', models.CharField(max_length=20, blank=True)),
                ('relationship', models.CharField(max_length=2, choices=[(b'Pa', b'Parent A'), (b'Pb', b'Parent B')])),
                ('family', models.ForeignKey(to='academics.Family')),
            ],
        ),
        migrations.CreateModel(
            name='StudentFamily',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('family_number', models.IntegerField()),
                ('family', models.ForeignKey(to='academics.Family')),
            ],
        ),
        migrations.CreateModel(
            name='StudentPermRec',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('student_id', models.CharField(unique=True, max_length=8)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('nickname', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='studentfamily',
            name='student',
            field=models.ForeignKey(to='academics.StudentPermRec'),
        ),
    ]
