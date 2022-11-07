from django.test import TestCase
from django.urls import reverse


class SignUpViewTest(TestCase):
    def test_signup_redict_to_home_page(self):
        data = {
            "username": "test123",
            "first_name": "Jean",
            "last_name": "Dujardin",
            "password1": "aStrongPassword",
            "password2": "aStrongPassword",
        }
        response = self.client.post(reverse("signup"), data)
        self.assertRedirects(response, "/home/")
