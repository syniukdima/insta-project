# Generated by Django 4.0 on 2023-12-02 15:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userchatmodel',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 2, 17, 15, 19, 231146)),
        ),
    ]