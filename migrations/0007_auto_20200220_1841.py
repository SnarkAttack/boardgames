# Generated by Django 3.0.3 on 2020-02-20 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boardgames', '0006_auto_20200220_1821'),
    ]

    operations = [
        migrations.RenameField(
            model_name='play',
            old_name='game_uuid',
            new_name='play_uuid',
        ),
    ]
