# Generated by Django 2.2.1 on 2020-07-27 18:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Forecast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_name', models.CharField(max_length=150)),
                ('cyclone_id', models.CharField(blank=True, max_length=10, null=True)),
                ('cyclone_name', models.CharField(blank=True, max_length=200, null=True)),
                ('image_link', models.CharField(blank=True, max_length=500, null=True)),
                ('time_of_last_forecast', models.DateTimeField(default=datetime.datetime.now)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
