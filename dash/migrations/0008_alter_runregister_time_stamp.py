# Generated by Django 4.0.6 on 2022-08-17 18:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0007_alter_runregister_time_stamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='runregister',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]