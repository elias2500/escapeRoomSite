# Generated by Django 4.1 on 2023-10-23 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0011_alter_room_userid_alter_room_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='title',
            field=models.CharField(default='A room', max_length=50, unique=True),
        ),
    ]