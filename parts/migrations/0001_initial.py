# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'Nazwa czesci')),
                ('id_name', models.CharField(max_length=100, verbose_name=b'Numer czesci')),
                ('parttype', models.CharField(default=b'sr', max_length=10, verbose_name=b'Typ czesci', choices=[(b'sp', b'sprezyna'), (b'sr', b'sruba'), (b'lo', b'lozysko')])),
                ('pic', models.ImageField(upload_to=b'images/')),
            ],
        ),
    ]
