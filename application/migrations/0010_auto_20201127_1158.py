# Generated by Django 3.1.2 on 2020-11-27 19:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0009_auto_20201127_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airline',
            name='added_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 27, 11, 58, 52, 864985), editable=False),
        ),
        migrations.AlterField(
            model_name='airplane',
            name='added_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 27, 11, 58, 52, 872986), editable=False),
        ),
    ]
