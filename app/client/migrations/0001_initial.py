# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id_client', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('slug', models.SlugField(null=True)),
                ('icon', models.CharField(max_length=155, null=True)),
                ('keywords', models.CharField(max_length=155, null=True)),
                ('author', models.CharField(max_length=155, null=True)),
                ('description', models.CharField(max_length=155, null=True)),
                ('color', models.CharField(max_length=155, null=True)),
                ('image', models.CharField(max_length=155, null=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.SmallIntegerField(default=1)),
            ],
            options={
                'db_table': 'client',
            },
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id_login', models.AutoField(serialize=False, primary_key=True)),
                ('email', models.CharField(max_length=250)),
                ('password', models.CharField(max_length=250)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.SmallIntegerField(default=1)),
                ('client', models.ForeignKey(to='client.Client')),
            ],
            options={
                'db_table': 'login',
            },
        ),
    ]
