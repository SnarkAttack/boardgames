# Generated by Django 3.0.2 on 2020-02-19 02:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boardgames', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Play',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(max_length=36)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boardgames.BoardGame')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_name', models.CharField(max_length=32)),
                ('bgg_name', models.CharField(max_length=32)),
            ],
        ),
        migrations.AlterField(
            model_name='boardgameexpansion',
            name='base_game',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='expansions', to='boardgames.BoardGame'),
        ),
        migrations.CreateModel(
            name='PlayerResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('winner', models.BooleanField()),
                ('play', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='play', to='boardgames.Play')),
                ('player', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player', to='boardgames.Player')),
            ],
        ),
        migrations.AddField(
            model_name='boardgame',
            name='owners',
            field=models.ManyToManyField(to='boardgames.Player'),
        ),
    ]
