# Generated by Django 2.0.3 on 2018-03-13 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mygym', '0002_auto_20180313_1457'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plan',
            old_name='plan',
            new_name='user',
        ),
    ]
