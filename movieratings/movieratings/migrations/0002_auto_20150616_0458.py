# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieratings', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ratings',
            name='movie',
        ),
        migrations.RemoveField(
            model_name='ratings',
            name='rater',
        ),
        migrations.DeleteModel(
            name='Movies',
        ),
        migrations.DeleteModel(
            name='Rater',
        ),
        migrations.DeleteModel(
            name='Ratings',
        ),
    ]
