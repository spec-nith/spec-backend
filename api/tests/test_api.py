from datetime import date

from rest_framework import status
from rest_framework.test import APITestCase

from api.models import Alumni, Blog, Gallery, Project, TeamModel, Workshop


class TeamModelTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        TeamModel.objects.create(
            name="team member",
            title="volunteer",
            description="skills",
            github_id="https://github.com/tm",
            linkedin_id="https://www.linkedin.com/tm",
            profile_pic=None,
        )

    def test_team_model_api_post(self):
        url = "/api/team/"
        data = {"name": "team member", "title": "volunteer"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_team_model_api_get(self):
        url = "/api/team/"
        data = {
            "id": 1,
            "name": "team member",
            "title": "volunteer",
            "description": "skills",
            "github_id": "https://github.com/tm",
            "linkedin_id": "https://www.linkedin.com/tm",
            "profile_pic_url": None,
        }
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        result = response.json()[0]
        self.assertEqual(result, data)


class BlogTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        Blog.objects.create(
            title="first blog",
            description="blog description here",
            author="ABC",
            body='{"key":"value"}',
        )

    def test_blog_api_post(self):
        url = "/api/blog/"
        data = {
            "title": "first blog",
            "description": "blog description here",
            "author": "ABC",
            "body": '{"key":"value"}',
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_blog_api_get(self):
        url = "/api/blog/"
        data = {
            "id": 1,
            "title": "first blog",
            "description": "blog description here",
            "author": "ABC",
            "body": '{"key":"value"}',
            "cover_url": None,
            "published": date.today().strftime("%Y-%m-%d"),
        }
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        result = response.json()[0]
        self.assertEqual(result, data)


class WorkshopTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        Workshop.objects.create(
            title="first workshop",
            description="workshop description here",
            event_date="2019-09-25T11:30:00+05:30",
            venue="XYZ",
        )

    def test_workshop_api_post(self):
        url = "/api/workshop/"
        data = {
            "id": 1,
            "title": "first workshop",
            "description": "workshop description here",
            "event_date": "2019-09-25T11:30:00+05:30",
            "venue_url": "XYZ",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_workshop_api_get(self):
        url = "/api/workshop/"
        data = {
            "id": 1,
            "title": "first workshop",
            "description": "workshop description here",
            "event_date": "2019-09-25T11:30:00+05:30",
            "venue": "XYZ",
            "cover_url": None,
        }
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        result = response.json()[0]
        self.assertEqual(result, data)


class GalleryTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        Gallery.objects.create(event="abc event", year=2019, sub_event="xyz event")

    def test_gallery_api_post(self):
        url = "/api/gallery/"
        data = {"event": "abc event", "year": "2019", "sub_event": "xyz event"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_gallery_api_get(self):
        url = "/api/gallery/"
        data = {
            "id": 1,
            "event": "abc event",
            "year": 2019,
            "sub_event": "xyz event",
            "image_url": None,
        }
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        result = response.json()[0]
        self.assertEqual(result, data)


class AlumniTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        Alumni.objects.create(
            name="alumni user",
            batch=2017,
            company="abc company",
            github_id="https://github.com/abc",
            linkedin_id="https://www.linkedin.com/",
        )

    def test_alumni_api_post(self):
        url = "/api/alumni/"
        data = {
            "id": 1,
            "name": "alumni user",
            "batch": 2017,
            "company": "abc company",
            "github_id": "https://github.com/abc",
            "linkedin_id": "https://www.linkedin.com/",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_alumni_api_get(self):
        url = "/api/alumni/"
        data = {
            "id": 1,
            "name": "alumni user",
            "batch": 2017,
            "dual_degree": False,
            "company": "abc company",
            "github_id": "https://github.com/abc",
            "linkedin_id": "https://www.linkedin.com/",
            "profile_pic_url": None,
        }
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        result = response.json()[0]
        self.assertEqual(result, data)


class ProjectTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        Project.objects.create(
            domain="project domain",
            name="first project",
            description="project description here",
            year=2019,
            github_link="https://github.com/project",
        )

    def test_project_api_post(self):
        url = "/api/projects/"
        data = {
            "id": 1,
            "domain": "project domain",
            "name": "first project",
            "description": "project description here",
            "year": 2019,
            "github_link": "https://github.com/project",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_project_api_get(self):
        url = "/api/projects/"
        data = {
            "id": 1,
            "domain": "project domain",
            "name": "first project",
            "description": "project description here",
            "year": 2019,
            "github_link": "https://github.com/project",
            "cover_url": None,
        }
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        result = response.json()[0]
        self.assertEqual(result, data)
