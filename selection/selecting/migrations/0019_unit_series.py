# Generated by Django 4.1.5 on 2023-06-13 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('selecting', '0018_series_alter_unit_compressor_alter_unit_evaporator_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='series',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='series', to='selecting.series'),
        ),
    ]
