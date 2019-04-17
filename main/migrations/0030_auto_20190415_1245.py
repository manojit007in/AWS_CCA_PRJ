# Generated by Django 2.1.7 on 2019-04-15 19:45

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_auto_20190415_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='article_id',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='articles',
            name='author',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='articles',
            name='profile_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Profiles', verbose_name='Profile'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='source_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Sources', verbose_name='Source'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='source_type_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Source_Types', verbose_name='Source Type'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='article_id',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Articles', verbose_name='Article'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='profile_id',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Profiles', verbose_name='Profile'),
        ),
        migrations.AlterField(
            model_name='query_runs',
            name='query_runtime',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 15, 12, 45, 48, 190396), verbose_name='Query Runtime'),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 15, 12, 45, 48, 187395), verbose_name='date published'),
        ),
    ]
