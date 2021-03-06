# Generated by Django 3.1.2 on 2020-11-26 22:53

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('application', '0007_auto_20201126_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airline',
            name='added_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 26, 14, 53, 11, 691547), editable=False),
        ),
        migrations.CreateModel(
            name='airline_staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('which_airline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.airline')),
                ('which_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
