# Generated by Django 5.0.6 on 2024-05-09 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_remove_branduser_is_superuser_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="branduser",
            name="last_login",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="customuser",
            name="last_login",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
