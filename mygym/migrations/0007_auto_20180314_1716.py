# Generated by Django 2.0.3 on 2018-03-14 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mygym', '0006_auto_20180314_1548'),
    ]

    operations = [
        migrations.RenameField(
            model_name='day',
            old_name='excercise',
            new_name='exercise',
        ),
    ]
