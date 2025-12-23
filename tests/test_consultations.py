from .base import AuthenticatedAPITestCase
from rest_framework import status
from datetime import timedelta
from django.utils import timezone
from django.urls import reverse
from core.models import Professional


class ConsultationsAPITests(AuthenticatedAPITestCase):
    def setUp(self):
        self.authenticate()
        self._url = reverse("consultation")
        self.prof = Professional.objects.create(
            social_name="João",
            profession="Clínico Geral",
            phone="19999999999",
            email="",
            street="Rua A",
            number="10",
            complement="",
            neighborhood="Centro",
            city="Paulinia",
        )
        self.payload: dict = {
            "professional": self.prof.id,
            "client_name": "Paciente X",
            "scheduled_at": (timezone.now() + timedelta(days=1)).isoformat(),
            "notes": "Primeira consulta",
        }
        return super().setUp()

    def test_list_consultations(self):
        response = self.client.get(self._url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_retrieve_update_destroy_consultations(self):

        # Create
        response_create = self.client.post(self._url, data=self.payload, format="json")
        self.assertEqual(response_create.status_code, status.HTTP_201_CREATED)
        data = response_create.data

        # Retrieve
        response_retrive = self.client.get(f"{self._url}{data['id']}/")
        self.assertEqual(response_retrive.status_code, status.HTTP_200_OK)

        # Update
        response_update = self.client.patch(
            f"{self._url}{data['id']}/",
            data={
                "client_name": "Paciente Y",
                "notes": "Editado Primeira consulta",
            },
            format="json",
        )
        self.assertEqual(response_update.status_code, status.HTTP_200_OK)

        # Destroy
        response_destroy = self.client.delete(f"{self._url}{data['id']}/")
        self.assertEqual(response_destroy.status_code, status.HTTP_204_NO_CONTENT)

    def test_list_consultations_for_professional(self):
        response = self.client.get(
            f"{self._url}?professional_id={self.prof.id}",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
