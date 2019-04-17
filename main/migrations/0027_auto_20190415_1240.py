# Generated by Django 2.1.7 on 2019-04-15 19:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_auto_20190415_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='article_raw',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='articles',
            name='source_url',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='query_runs',
            name='query_runtime',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 15, 12, 40, 33, 747895), verbose_name='Query Runtime'),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 15, 12, 40, 33, 744898), verbose_name='date published'),
        ),
    ]
