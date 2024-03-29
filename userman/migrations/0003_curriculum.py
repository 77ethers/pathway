# Generated by Django 4.2.3 on 2023-08-03 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("userman", "0002_alter_user_daily_time_dedication_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Curriculum",
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
                ("curriculum_text", models.TextField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="userman.user"
                    ),
                ),
            ],
        ),
    ]
