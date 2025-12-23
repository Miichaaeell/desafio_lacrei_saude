from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse


class AuthRequiredTests(APITestCase):
    def test_get_token_forbidden(self):
        url = reverse("token_obtain_pair")
        res = self.client.post(url, data={}, format="json")
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
