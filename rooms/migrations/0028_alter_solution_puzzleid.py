# Generated by Django 4.1 on 2023-11-28 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0027_alter_puzzle_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solution',
            name='puzzleId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solutions', to='rooms.puzzle'),
        ),
    ]
