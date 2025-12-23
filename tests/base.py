from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from django.urls import reverse


class AuthenticatedAPITestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        User = get_user_model()
        cls.user_password = "testpassword123"
        cls.user = User.objects.create_superuser(
            username="testuser", password=cls.user_password
        )

    def authenticate(self):
        url = reverse("token_obtain_pair")
        response = self.client.post(
            url,
            data={"username": self.user.username, "password": self.user_password},
            format="json",
        )
        self.assertEqual(response.status_code, 200, response.data)
        token = response.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
