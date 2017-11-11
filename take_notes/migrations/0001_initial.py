# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserNotes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.IntegerField(default=0)),
                ('modified_on', models.DateTimeField(auto_now_add=True)),
                ('modified_by', models.IntegerField(default=0)),
                ('title', models.CharField(max_length=50)),
                ('text', models.CharField(max_length=1000)),
            ],
        ),
    ]
