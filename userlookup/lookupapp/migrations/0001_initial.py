# Generated by Django 2.2.6 on 2019-10-17 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('birdthday', models.DateField()),
                ('address', models.CharField(max_length=20)),
            ],
        ),
    ]
