# Generated by Django 5.1.3 on 2024-12-29 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0005_rename_data_foto_fotografia_data_fotografia_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotografia',
            name='categoria',
            field=models.CharField(blank=True, choices=[('Nebulosa', 'Nebulosa'), ('Estrela', 'Estrela'), ('Galáxia', 'Galáxia'), ('Planeta', 'Planeta')], default='', max_length=100, null=True),
        ),
    ]
