from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from model_bakery import baker


class StudyPlanAPITest(APITestCase):
    def setUp(self):
        self.study_plans = baker.make("api.StudyPlan", _quantity=10)

    def test_create_study_plan(self):
        url = reverse("studyplan-list")
        data = {
            "user": self.study_plans[0].user.id,
            "name": "*",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_study_plan_list(self):
        url = reverse("studyplan-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_study_plan_detail(self):
        url = reverse("studyplan-detail", args=[self.study_plans[0].id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
