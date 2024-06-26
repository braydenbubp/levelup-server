# Generated by Django 4.1.3 on 2024-05-21 00:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('levelupapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='levelupapi.game'),
        ),
        migrations.AlterField(
            model_name='event',
            name='organizer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='levelupapi.gamer'),
        ),
        migrations.AlterField(
            model_name='game',
            name='game_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='levelupapi.gametype'),
        ),
        migrations.AlterField(
            model_name='game',
            name='gamer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='levelupapi.gamer'),
        ),
        migrations.AlterField(
            model_name='game',
            name='number_of_players',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='game',
            name='skill_level',
            field=models.IntegerField(default=0),
        ),
    ]
