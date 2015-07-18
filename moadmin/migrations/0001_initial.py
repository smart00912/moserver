# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModuleList',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column=b'ID')),
                ('module_name', models.CharField(max_length=100)),
                ('module_fun_desc', models.CharField(max_length=500)),
                ('module_fun_ext', models.CharField(max_length=5000)),
            ],
            options={
                'db_table': 'module_list',
            },
        ),
        migrations.CreateModel(
            name='ServerAppCateg',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column=b'ID')),
                ('app_categ_name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'server_app_categ',
            },
        ),
        migrations.CreateModel(
            name='ServerFunCateg',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column=b'ID')),
                ('server_categ_name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'server_fun_categ',
            },
        ),
        migrations.CreateModel(
            name='ServerList',
            fields=[
                ('server_name', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('server_extip', models.CharField(max_length=45)),
                ('server_intip', models.CharField(max_length=45)),
                ('server_os', models.CharField(max_length=50)),
                ('server_app_id', models.ForeignKey(to='moadmin.ServerAppCateg')),
            ],
            options={
                'db_table': 'server_list',
            },
        ),
        migrations.AddField(
            model_name='serverappcateg',
            name='server_categ_id',
            field=models.ForeignKey(to='moadmin.ServerFunCateg'),
        ),
    ]
