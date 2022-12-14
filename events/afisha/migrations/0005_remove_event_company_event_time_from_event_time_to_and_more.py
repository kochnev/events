# Generated by Django 4.0.6 on 2022-08-03 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('afisha', '0004_event_currency'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='company',
        ),
        migrations.AddField(
            model_name='event',
            name='time_from',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='time_to',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='date_from',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='date_to',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='poster',
            field=models.ImageField(upload_to='events'),
        ),
    ]
