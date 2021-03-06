# Generated by Django 3.1.6 on 2021-02-23 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AnimeList', '0006_auto_20210223_2309'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='duration',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=256, null=True),
        ),
        migrations.AddField(
            model_name='anime',
            name='genres',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='anime',
            name='ranked',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='anime',
            name='rating',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='anime',
            name='score',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='anime',
            name='source',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
