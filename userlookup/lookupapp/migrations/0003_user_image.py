# Generated by Django 2.2.6 on 2019-11-08 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lookupapp', '0002_auto_20191017_0150'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.URLField(default=''),
        ),
    ]