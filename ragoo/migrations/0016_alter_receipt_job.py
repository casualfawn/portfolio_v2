# Generated by Django 4.0.2 on 2024-08-05 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ragoo', '0015_rename_client_receipt_client_name_alter_receipt_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt',
            name='Job',
            field=models.TextField(),
        ),
    ]
