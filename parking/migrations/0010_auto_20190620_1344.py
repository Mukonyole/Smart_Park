# Generated by Django 2.2.1 on 2019-06-20 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0009_auto_20190620_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicleentry',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
