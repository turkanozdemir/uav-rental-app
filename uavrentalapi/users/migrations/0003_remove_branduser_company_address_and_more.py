# Generated by Django 5.0.6 on 2024-05-09 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_alter_branduser_address_alter_branduser_company_name_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="branduser",
            name="company_address",
        ),
        migrations.RemoveField(
            model_name="branduser",
            name="contact_info",
        ),
    ]
