# Generated by Django 4.0.6 on 2023-04-08 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('afisha', '0012_rename_url_event_event_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='for_kids',
            field=models.BooleanField(default=False, verbose_name='Детский'),
        ),
    ]
