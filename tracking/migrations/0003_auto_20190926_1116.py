# Generated by Django 2.0.13 on 2019-09-26 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0002_auto_20180918_2014'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitor',
            name='medium',
            field=models.CharField(blank=True, editable=False, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='visitor',
            name='source',
            field=models.CharField(blank=True, editable=False, max_length=255, null=True),
        ),
    ]