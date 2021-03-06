# Generated by Django 2.1.7 on 2019-04-15 19:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0035_auto_20190415_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hashtags',
            name='hashtag_id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='Hashtag ID'),
        ),
        migrations.AlterField(
            model_name='keyword_categories',
            name='keyword_category_id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='Keyword Category ID'),
        ),
        migrations.AlterField(
            model_name='profiles',
            name='profile_id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='Profile Id'),
        ),
        migrations.AlterField(
            model_name='query_runs',
            name='query_runtime',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 15, 12, 56, 20, 291528), verbose_name='Query Runtime'),
        ),
        migrations.AlterField(
            model_name='rank',
            name='result_id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='Rank Id'),
        ),
        migrations.AlterField(
            model_name='replies',
            name='reply_id',
            field=models.BigAutoField(primary_key=True, serialize=False, verbose_name='Reply ID (System)'),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 15, 12, 56, 20, 288528), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='tweets',
            name='tweet_id',
            field=models.BigAutoField(primary_key=True, serialize=False, verbose_name='Tweet ID (System)'),
        ),
    ]
