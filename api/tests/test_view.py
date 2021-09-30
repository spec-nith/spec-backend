from django.contrib.auth.models import User
from django.http import request, response
from django.test import TestCase
from django.urls import reverse


class HomeViewTest(TestCase):
    def test_home_url_exists(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_home_url_accessible_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "I'm on")


class GalleryFormViewTest(TestCase):
    def test_gallery_url_exists(self):
        response = self.client.get("/gallery/")
        self.assertEqual(response.status_code, 302)

    def test_gallery_url_accessible_by_name(self):
        response = self.client.get(reverse("gallery"))
        self.assertEqual(response.status_code, 302)

    def test_gallery_auth(self):
        user = User.objects.create_user("username", "user@test.com", "password")
        self.client.force_login(user=user)
        response = self.client.get("/gallery/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "gallery.html")
