# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.CharField(max_length=400, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='NewPerson',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('session_id', models.CharField(max_length=20, blank=True)),
                ('time', models.DateTimeField(default=datetime.datetime.now)),
                ('connected', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Pairing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user1', models.ForeignKey(related_name='first', to='app.NewPerson')),
                ('user2', models.ForeignKey(related_name='second', to='app.NewPerson')),
            ],
        ),
        migrations.CreateModel(
            name='Waiting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('session_id', models.OneToOneField(to='app.NewPerson')),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='session_id',
            field=models.ForeignKey(to='app.NewPerson'),
        ),
    ]
