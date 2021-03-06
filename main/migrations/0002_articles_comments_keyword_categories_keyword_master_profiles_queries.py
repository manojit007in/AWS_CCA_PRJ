# Generated by Django 2.1.7 on 2019-04-14 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_id', models.BigIntegerField()),
                ('title', models.CharField(max_length=255)),
                ('source_id', models.IntegerField()),
                ('source_type_id', models.IntegerField()),
                ('profile_id', models.BigIntegerField()),
                ('source_url', models.TextField()),
                ('article_raw', models.TextField()),
                ('author', models.CharField(max_length=200)),
                ('public', models.IntegerField()),
                ('owner', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_id', models.BigIntegerField()),
                ('article_id', models.BigIntegerField()),
                ('profile_id', models.BigIntegerField()),
                ('source_id', models.IntegerField()),
                ('comment_raw', models.TextField()),
                ('parent_comment_id', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Keyword_Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword_category_id', models.IntegerField()),
                ('category', models.CharField(max_length=100)),
                ('system', models.IntegerField()),
                ('public', models.IntegerField()),
                ('owner', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Keyword_Master',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword_id', models.IntegerField()),
                ('keyword', models.CharField(max_length=200)),
                ('keyword_category_id', models.IntegerField()),
                ('default_weight', models.FloatField()),
                ('system', models.IntegerField()),
                ('owner', models.IntegerField()),
                ('public', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Profiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_id', models.BigIntegerField()),
                ('profile', models.CharField(max_length=200)),
                ('source_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Queries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query_id', models.IntegerField()),
                ('query', models.TextField()),
                ('override', models.IntegerField()),
                ('system', models.IntegerField()),
                ('public', models.IntegerField()),
                ('owner', models.IntegerField()),
            ],
        ),
    ]
