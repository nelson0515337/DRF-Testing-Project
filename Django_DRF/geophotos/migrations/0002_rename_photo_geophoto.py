# Generated by Django 4.2.9 on 2024-08-04 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geophotos', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Photo',
            new_name='GeoPhoto',
        ),
    ]