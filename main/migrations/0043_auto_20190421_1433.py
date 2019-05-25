# Generated by Django 2.1.7 on 2019-04-21 21:33

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0042_auto_20190421_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query_runs',
            name='query_runtime',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 21, 14, 33, 26, 999952), verbose_name='Query Runtime'),
        ),
        migrations.AlterField(
            model_name='rank',
            name='article_id',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.Articles', verbose_name='Article Id'),
        ),
        migrations.AlterField(
            model_name='rank',
            name='query_run_id',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.Query_Runs', verbose_name='Query Run Id'),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 21, 14, 33, 26, 996952), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='twitter_imports',
            name='run_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 21, 14, 33, 27, 953), verbose_name='Run Time'),
        ),
    ]