# Generated by Django 2.1.7 on 2019-04-15 00:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20190414_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query_runs',
            name='query_runtime',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 14, 17, 50, 45, 314916), verbose_name='Query Runtime'),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 14, 17, 50, 45, 312916), verbose_name='date published'),
        ),
    ]
