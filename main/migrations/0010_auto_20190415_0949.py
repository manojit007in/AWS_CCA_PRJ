# Generated by Django 2.1.7 on 2019-04-15 16:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20190415_0917'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hashtags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hashtag_id', models.IntegerField(verbose_name='Hashtag Id')),
                ('hashtag_string', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Replies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tweet_id', models.BigIntegerField()),
                ('created_at', models.DateTimeField()),
                ('id_str', models.CharField(max_length=255)),
                ('tweet_text', models.CharField(max_length=255)),
                ('in_reply_to_status_id_str', models.CharField(max_length=255)),
                ('in_reply_to_user_id_str', models.CharField(max_length=255)),
                ('n_reply_to_screen_name', models.CharField(max_length=255)),
                ('user_name', models.CharField(max_length=255)),
                ('user_screen_name', models.CharField(max_length=255)),
                ('entities_hashtags', models.CharField(max_length=255)),
                ('entities_urls', models.CharField(max_length=255)),
                ('entities_user_mentions', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Tweets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tweet_id', models.BigIntegerField()),
                ('created_at', models.DateTimeField()),
                ('id_str', models.CharField(max_length=255)),
                ('tweet_text', models.CharField(max_length=255)),
                ('in_reply_to_status_id_str', models.CharField(max_length=255)),
                ('in_reply_to_user_id_str', models.CharField(max_length=255)),
                ('n_reply_to_screen_name', models.CharField(max_length=255)),
                ('user_name', models.CharField(max_length=255)),
                ('user_screen_name', models.CharField(max_length=255)),
                ('entities_hashtags', models.CharField(max_length=255)),
                ('entities_urls', models.CharField(max_length=255)),
                ('entities_user_mentions', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='query_runs',
            name='query_runtime',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 15, 9, 49, 0, 956244), verbose_name='Query Runtime'),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 15, 9, 49, 0, 954245), verbose_name='date published'),
        ),
    ]