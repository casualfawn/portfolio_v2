# Generated by Django 4.0.2 on 2024-08-05 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ragoo', '0013_rename_client_name_receipt_client_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='receipt',
            old_name='profession',
            new_name='Job',
        ),
    ]