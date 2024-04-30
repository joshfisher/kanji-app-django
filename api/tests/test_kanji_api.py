from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from model_bakery import baker


# Create your tests here.
class KanjiViewSetTests(APITestCase):

    def setUp(self):
        self.kanji = baker.make("api.Kanji", _quantity=10)

    def test_list_kanji(self):
        url = reverse("kanji-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_kanji(self):
        url = reverse("kanji-detail", args=[self.kanji[0].id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_kanji(self):
        url = reverse("kanji-list")
        data = {
            "character": "*",
            "meaning": "**",
            "on_reading": "****",
            "kun_reading": "*****",
            "jlpt_level": 5,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
