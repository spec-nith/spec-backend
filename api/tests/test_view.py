from django.contrib.auth.models import User
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


class WorkshopFormViewTest(TestCase):
    def test_workshop_url_exists(self):
        response = self.client.get("/workshop/")
        self.assertEqual(response.status_code, 302)

    def test_workshop_url_accessible_by_name(self):
        response = self.client.get(reverse("workshop"))
        self.assertEqual(response.status_code, 302)

    def test_workshop_auth(self):
        user = User.objects.create_user("username", "user@test.com", "password")
        self.client.force_login(user=user)
        response = self.client.get("/workshop/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "workshop.html")


class TeamModelCreateViewTest(TestCase):
    def test_team_url_exists(self):
        response = self.client.get("/team/")
        self.assertEqual(response.status_code, 302)

    def test_team_url_accessible_by_name(self):
        response = self.client.get(reverse("team"))
        self.assertEqual(response.status_code, 302)

    def test_team_auth(self):
        user = User.objects.create_user("username", "user@test.com", "password")
        self.client.force_login(user=user)
        response = self.client.get("/team/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "team.html")


class AlumniCreateViewTest(TestCase):
    def test_alumni_url_exists(self):
        response = self.client.get("/alumni/")
        self.assertEqual(response.status_code, 302)

    def test_alumni_url_accessible_by_name(self):
        response = self.client.get(reverse("alumni"))
        self.assertEqual(response.status_code, 302)

    def test_alumni_auth(self):
        user = User.objects.create_user("username", "user@test.com", "password")
        self.client.force_login(user=user)
        response = self.client.get("/alumni/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "alumni.html")


class ProjectCreateViewTest(TestCase):
    def test_project_url_exists(self):
        response = self.client.get("/project/")
        self.assertEqual(response.status_code, 302)

    def test_project_url_accessible_by_name(self):
        response = self.client.get(reverse("project"))
        self.assertEqual(response.status_code, 302)

    def test_project_auth(self):
        user = User.objects.create_user("username", "user@test.com", "password")
        self.client.force_login(user=user)
        response = self.client.get("/project/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "project.html")
