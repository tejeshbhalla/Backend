# Generated by Django 3.2.2 on 2023-04-02 07:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0007_auto_20230402_0722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group_logs',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 2, 7, 26, 46, 557512)),
        ),
        migrations.AlterField(
            model_name='user_logs',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 2, 7, 26, 46, 556512)),
        ),
    ]
