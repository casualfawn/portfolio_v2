# Generated by Django 4.0.2 on 2024-08-05 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ragoo', '0014_rename_profession_receipt_job'),
    ]

    operations = [
        migrations.RenameField(
            model_name='receipt',
            old_name='client',
            new_name='client_name',
        ),
        migrations.AlterField(
            model_name='receipt',
            name='Job',
            field=models.IntegerField(),
        ),
    ]