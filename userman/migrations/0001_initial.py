# Generated by Django 4.2.3 on 2023-07-31 19:44

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("name", models.CharField(max_length=100)),
                ("whatsapp_number", models.CharField(max_length=15)),
                ("learning_goal", models.CharField(max_length=100)),
                ("target_date", models.DateField()),
                ("current_skill_level", models.IntegerField()),
                ("sub_skills", models.TextField()),
                ("daily_time_dedication", models.DurationField()),
                ("preferred_learning_time", models.TimeField()),
                ("learning_preference", models.CharField(max_length=50)),
                ("progress_tracking_preference", models.BooleanField(default=False)),
                (
                    "chat_state",
                    models.CharField(default="awaiting_name", max_length=50),
                ),
                (
                    "last_interaction_timestamp",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Progress",
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
                ("task_completed", models.TextField()),
                ("completion_date", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="userman.user"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Notification",
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
                ("notification_text", models.TextField()),
                ("sent_timestamp", models.DateTimeField(auto_now_add=True)),
                ("feedback", models.TextField(blank=True, null=True)),
                ("feedback_timestamp", models.DateTimeField(blank=True, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="userman.user"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="LearningPathway",
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
                ("pathway_text", models.TextField()),
                ("generation_timestamp", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="userman.user"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Interaction",
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
                ("interaction_text", models.TextField()),
                ("interaction_timestamp", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="userman.user"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DailyTask",
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
                ("task_text", models.TextField()),
                ("due_date", models.DateField()),
                ("completion_status", models.BooleanField(default=False)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="userman.user"
                    ),
                ),
            ],
        ),
    ]
