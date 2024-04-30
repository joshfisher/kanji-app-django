from django.db import models
from django.contrib.auth.models import User


class Kanji(models.Model):
    JLPT_LEVEL_CHOICES = (
        (1, "N1"),
        (2, "N2"),
        (3, "N3"),
        (4, "N4"),
        (5, "N5"),
    )

    character = models.CharField(max_length=1)
    jlpt_level = models.IntegerField(choices=JLPT_LEVEL_CHOICES)
    meaning = models.CharField(max_length=255)
    on_reading = models.CharField(max_length=255)
    kun_reading = models.CharField(max_length=255)


class StudyPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)


class Flashcard(models.Model):
    kanji = models.ForeignKey(Kanji, on_delete=models.CASCADE)
    study_plan = models.ForeignKey(StudyPlan, on_delete=models.CASCADE)
    front_text = models.CharField(max_length=255)
    back_text = models.CharField(max_length=255)
    times_seen = models.IntegerField(default=0)
    times_correct = models.IntegerField(default=0)
    times_passed = models.IntegerField(default=0)
    last_time_seen = models.DateTimeField(null=True, blank=True)
