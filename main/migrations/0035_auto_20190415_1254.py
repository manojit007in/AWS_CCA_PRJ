# Generated by Django 2.1.7 on 2019-04-15 19:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0034_auto_20190415_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='queries',
            name='query_id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='Query ID'),
        ),
        migrations.AlterField(
            model_name='query_runs',
            name='query_runtime',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 15, 12, 54, 25, 230817), verbose_name='Query Runtime'),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 15, 12, 54, 25, 227817), verbose_name='date published'),
        ),
    ]
