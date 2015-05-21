# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_delete_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=30)),
                ('fname', models.CharField(max_length=30)),
                ('lname', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('school', models.CharField(max_length=200)),
                ('school_year', models.IntegerField()),
                ('pub_date', models.DateTimeField(verbose_name=b'Date published')),
                ('enable_comments', models.BooleanField(default=True)),
            ],
        ),
    ]
