# Generated by Django 4.1 on 2023-10-13 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0004_alter_room_maxplayers_alter_room_minplayers_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Puzzle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='A puzzle', max_length=50)),
                ('relatedPuzzle', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rooms.puzzle')),
            ],
        ),
        migrations.AddField(
            model_name='room',
            name='brief',
            field=models.TextField(default='A brief'),
        ),
        migrations.AddField(
            model_name='room',
            name='debrief',
            field=models.TextField(default='A debrief'),
        ),
        migrations.AddField(
            model_name='room',
            name='difficulty',
            field=models.CharField(default='Easy', max_length=10),
        ),
        migrations.AddField(
            model_name='room',
            name='goal',
            field=models.CharField(default='A goal', max_length=50),
        ),
        migrations.AddField(
            model_name='room',
            name='hasActor',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='room',
            name='theme',
            field=models.CharField(default='None', max_length=50),
        ),
        migrations.AddField(
            model_name='room',
            name='timeLimit',
            field=models.TimeField(default='00:30:00'),
        ),
        migrations.CreateModel(
            name='SubRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='A subroom', max_length=50)),
                ('roomId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.room')),
            ],
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(default='A description')),
                ('puzzleId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.puzzle')),
            ],
        ),
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(default='A description')),
                ('puzzleId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.puzzle')),
            ],
        ),
        migrations.AddField(
            model_name='puzzle',
            name='subRoomId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.subroom'),
        ),
        migrations.CreateModel(
            name='Hint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(default='A description')),
                ('puzzleId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.puzzle')),
            ],
        ),
    ]
