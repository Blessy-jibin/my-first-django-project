# Generated by Django 2.0.3 on 2018-03-12 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True
    
    atomic = False

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Days',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Day_id', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Exercises',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Exercise_id', models.CharField(max_length=30, unique=True)),
                ('exercise_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, unique=True)),
                ('day1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='planday1', to='myapp.Days')),
                ('day2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='planday2', to='myapp.Days')),
                ('day3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='planday3', to='myapp.Days')),
                ('day4', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='planday4', to='myapp.Days')),
            ],
        ),
        migrations.AddField(
            model_name='days',
            name='exercise1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dayex1', to='myapp.Exercises'),
        ),
        migrations.AddField(
            model_name='days',
            name='exercise2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dayex2', to='myapp.Exercises'),
        ),
        migrations.AddField(
            model_name='days',
            name='exercise3',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dayex3', to='myapp.Exercises'),
        ),
        migrations.AddField(
            model_name='days',
            name='exercise4',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dayex4', to='myapp.Exercises'),
        ),
    ]
