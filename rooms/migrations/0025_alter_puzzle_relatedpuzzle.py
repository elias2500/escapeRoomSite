# Generated by Django 4.1 on 2023-11-28 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0024_alter_puzzle_subroomid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='puzzle',
            name='relatedPuzzle',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='relatedPuzzles', to='rooms.puzzle'),
        ),
    ]
