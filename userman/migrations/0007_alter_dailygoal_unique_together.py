# Generated by Django 4.2.3 on 2023-08-08 17:36

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("userman", "0006_dailygoal"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="dailygoal",
            unique_together=set(),
        ),
    ]