from rest_framework import serializers
from .models import Kanji, StudyPlan, Flashcard


class KanjiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kanji
        fields = "__all__"


class StudyPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyPlan
        fields = "__all__"


class FlashcardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flashcard
        fields = "__all__"
