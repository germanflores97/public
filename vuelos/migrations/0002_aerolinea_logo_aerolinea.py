# Generated by Django 2.2.24 on 2021-07-25 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vuelos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aerolinea',
            name='logo_aerolinea',
            field=models.ImageField(default='', upload_to='', verbose_name='Logo de la aerolínea'),
            preserve_default=False,
        ),
    ]
