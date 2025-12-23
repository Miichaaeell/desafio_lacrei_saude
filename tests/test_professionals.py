from rest_framework import status
from django.urls import reverse
from .base import AuthenticatedAPITestCase


class ProfessionalAPITest(AuthenticatedAPITestCase):
    def setUp(self):
        self._url = reverse("professional")
        self._payload: dict = {
            "social_name": "João",
            "profession": "Clínico Geral",
            "phone": "19999999999",
            "email": "",
            "street": "Rua A",
            "number": "10",
            "complement": "",
            "neighborhood": "Centro",
            "city": "Paulinia",
        }
        self.authenticate()
        return super().setUp()

    def test_list_professional(self):
        response = self.client.get(self._url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_retrieve_update_detele_professional(self):
        # Create
        response_create = self.client.post(self._url, data=self._payload, format="json")
        professional = response_create.data["id"]
        self.assertEqual(response_create.status_code, status.HTTP_201_CREATED)

        # Retrieve
        response_retrieve = self.client.get(f"{self._url}{professional}/")
        self.assertEqual(response_retrieve.status_code, status.HTTP_200_OK)

        # Update
        response_update = self.client.patch(
            f"{self._url}{professional}/",
            data={"profession": "Anestesista"},
            format="json",
        )
        self.assertEqual(response_update.status_code, status.HTTP_200_OK)

        # Destroy
        response_destroy = self.client.delete(f"{self._url}{professional}/")
        self.assertEqual(response_destroy.status_code, status.HTTP_204_NO_CONTENT)
