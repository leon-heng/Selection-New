# Generated by Django 4.1.5 on 2023-06-28 09:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selecting', '0037_floworientation_discharge_orientation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calculation',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 28, 17, 11, 12, 247151)),
        ),
        migrations.AlterField(
            model_name='history',
            name='generated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 28, 17, 11, 12, 248195)),
        ),
    ]
