# Generated by Django 4.2.3 on 2023-08-05 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("userman", "0005_notification_sent"),
    ]

    operations = [
        migrations.CreateModel(
            name="DailyGoal",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField()),
                ("goal_text", models.TextField()),
                ("is_completed", models.BooleanField(default=False)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="userman.user"
                    ),
                ),
            ],
            options={
                "unique_together": {("user", "date")},
            },
        ),
    ]