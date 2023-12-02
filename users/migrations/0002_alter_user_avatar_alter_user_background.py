# Generated by Django 4.0 on 2023-12-02 15:15

from django.db import migrations, models
import django.db.models.deletion
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ForeignKey(default=users.models.AvatarUser.defaultImg, on_delete=django.db.models.deletion.CASCADE, to='users.avataruser'),
        ),
        migrations.AlterField(
            model_name='user',
            name='background',
            field=models.ForeignKey(default=users.models.BackgroundUser.defaultImg, on_delete=django.db.models.deletion.CASCADE, to='users.backgrounduser'),
        ),
    ]