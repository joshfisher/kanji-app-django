from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r"kanji", views.KanjiViewSet)
router.register(r"studyplan", views.StudyPlanViewSet)
router.register(r"flashcard", views.FlashcardViewSet)

urlpatterns = [
    path("", include(router.urls)),
    # Add more paths for your views here
]
