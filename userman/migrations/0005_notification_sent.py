# Generated by Django 4.2.3 on 2023-08-04 03:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("userman", "0004_notification_notification_slug_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="notification",
            name="sent",
            field=models.BooleanField(default=False),
        ),
    ]
