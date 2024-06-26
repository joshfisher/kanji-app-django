# Generated by Django 5.0.4 on 2024-04-28 23:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Kanji",
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
                (
                    "jlpt_level",
                    models.IntegerField(
                        choices=[(1, "N1"), (2, "N2"), (3, "N3"), (4, "N4"), (5, "N5")]
                    ),
                ),
                ("meaning", models.CharField(max_length=255)),
                ("on_reading", models.CharField(max_length=255)),
                ("kun_reading", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="StudyPlan",
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
                ("name", models.CharField(max_length=255)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Flashcard",
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
                ("front_text", models.CharField(max_length=255)),
                ("back_text", models.CharField(max_length=255)),
                ("times_seen", models.IntegerField(default=0)),
                ("times_correct", models.IntegerField(default=0)),
                ("times_passed", models.IntegerField(default=0)),
                ("last_time_seen", models.DateTimeField(blank=True, null=True)),
                (
                    "kanji",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.kanji"
                    ),
                ),
                (
                    "study_plan",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.studyplan"
                    ),
                ),
            ],
        ),
    ]
