# Generated by Django 3.2.2 on 2023-03-23 10:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0002_auto_20230307_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group_logs',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 23, 10, 28, 6, 215855)),
        ),
        migrations.AlterField(
            model_name='user_logs',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 23, 10, 28, 6, 215855)),
        ),
    ]
