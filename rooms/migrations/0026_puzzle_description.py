# Generated by Django 4.1 on 2023-11-28 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0025_alter_puzzle_relatedpuzzle'),
    ]

    operations = [
        migrations.AddField(
            model_name='puzzle',
            name='description',
            field=models.TextField(default='A description'),
        ),
    ]