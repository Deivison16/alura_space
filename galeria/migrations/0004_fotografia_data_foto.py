# Generated by Django 5.1.3 on 2024-12-28 23:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0003_fotografia_publicada'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='data_foto',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
