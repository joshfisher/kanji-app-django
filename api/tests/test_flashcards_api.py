from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from model_bakery import baker


class FlashcardViewSetTests(APITestCase):

    def setUp(self):
        self.flashcard = baker.make("api.Flashcard", _quantity=10)

    def test_list_flashcard(self):
        url = reverse("flashcard-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_flashcard(self):
        url = reverse("flashcard-detail", args=[self.flashcard[0].id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_flashcard(self):
        url = reverse("flashcard-list")
        data = {
            "kanji": 1,
            "study_plan": 1,
            "front_text": "***",
            "back_text": "***",
            "times_seen": 0,
            "times_correct": 0,
            "times_passed": 0,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
