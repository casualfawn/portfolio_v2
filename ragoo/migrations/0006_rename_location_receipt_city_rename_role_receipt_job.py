# Generated by Django 4.0.2 on 2024-08-02 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ragoo', '0005_rename_client_name_receipt_person_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='receipt',
            old_name='Location',
            new_name='City',
        ),
        migrations.RenameField(
            model_name='receipt',
            old_name='Role',
            new_name='Job',
        ),
    ]
