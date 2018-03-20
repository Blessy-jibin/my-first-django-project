# Generated by Django 2.0.3 on 2018-03-14 12:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mygym', '0004_auto_20180313_2012'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='plan',
            name='user',
        ),
        migrations.AddField(
            model_name='userdata',
            name='plan',
            field=models.ManyToManyField(to='mygym.Plan'),
        ),
        migrations.AddField(
            model_name='userdata',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]