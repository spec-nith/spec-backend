from django.test import TestCase
from django.urls import reverse

class HomeViewTest(TestCase):
    def test_url_exists(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_accessible_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)