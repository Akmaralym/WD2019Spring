# Generated by Django 2.0.13 on 2019-05-06 11:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20190506_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 6, 11, 36, 0, 242938)),
        ),
    ]
