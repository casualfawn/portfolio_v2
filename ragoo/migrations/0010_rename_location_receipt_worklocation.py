# Generated by Django 4.0.2 on 2024-08-03 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ragoo', '0009_rename_city_location_receipt_location_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='receipt',
            old_name='location',
            new_name='worklocation',
        ),
    ]