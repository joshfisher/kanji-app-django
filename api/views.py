from django.shortcuts import render
from rest_framework import viewsets
from .models import Kanji, StudyPlan, Flashcard
from .serializers import KanjiSerializer, StudyPlanSerializer, FlashcardSerializer

# Create your views here.


class KanjiViewSet(viewsets.ModelViewSet):
    queryset = Kanji.objects.all()
    serializer_class = KanjiSerializer


class StudyPlanViewSet(viewsets.ModelViewSet):
    queryset = StudyPlan.objects.all()
    serializer_class = StudyPlanSerializer


class FlashcardViewSet(viewsets.ModelViewSet):
    queryset = Flashcard.objects.all()
    serializer_class = FlashcardSerializer
