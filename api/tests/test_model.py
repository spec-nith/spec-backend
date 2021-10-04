from django.core.exceptions import ValidationError
from django.core.files import File
from django.test import TestCase

from api.models import Alumni, Blog, Gallery, Project, TeamModel, Workshop
from api.test_settings import common_settings

DUMMY_PATH = "api/tests/dummy/test_image.jpeg"

# Create your tests here.
@common_settings
class TeamModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        TeamModel.objects.create(
            name="team user",
            title="Volunteer",
            github_id="https://github.com/tm",
            linkedin_id="https://www.linkedin.com/tm",
            profile_pic=File(open(DUMMY_PATH, "rb")),
        )

    def test_team_model_validation_error(self):
        team = TeamModel.objects.get(id=1)
        try:
            team.full_clean()
        except ValidationError as e:
            self.fail(e)

        team.github_id = "https://test.com/tm"
        team.linkedin_id = "https://www.test.com/tm"
        team.save()
        team.refresh_from_db()
        self.assertRaises(ValidationError, team.full_clean)

    def test_team_name(self):
        team = TeamModel.objects.get(id=1)
        expected_object_name = f"{team.name}"
        self.assertEquals(expected_object_name, "team user")

    def test_team_title(self):
        team = TeamModel.objects.get(id=1)
        expected_object_name = f"{team.title}"
        self.assertEquals(expected_object_name, "Volunteer")

    def test_team_github_id(self):
        team = TeamModel.objects.get(id=1)
        expected_object_name = f"{team.github_id}"
        self.assertEquals(expected_object_name, "https://github.com/tm")

    def test_team_linkedin_id(self):
        team = TeamModel.objects.get(id=1)
        expected_object_name = f"{team.linkedin_id}"
        self.assertEquals(expected_object_name, "https://www.linkedin.com/tm")

    def test_team_profile_pic(self):
        team = TeamModel.objects.get(id=1)
        team.update_team_image_url()
        team.refresh_from_db()
        expected_object_name = f"{team.profile_pic.url}"
        self.assertEquals(expected_object_name, team.profile_pic_url)


@common_settings
class BlogTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Blog.objects.create(
            title="first blog",
            description="blog description here",
            author="ABC",
            body='{"key":"value"}',
            cover=File(open(DUMMY_PATH, "rb")),
        )

    def test_blog_title(self):
        blog = Blog.objects.get(id=1)
        expected_object_name = f"{blog.title}"
        self.assertEquals(expected_object_name, "first blog")

    def test_blog_description(self):
        blog = Blog.objects.get(id=1)
        expected_object_name = f"{blog.description}"
        self.assertEquals(expected_object_name, "blog description here")

    def test_blog_author(self):
        blog = Blog.objects.get(id=1)
        expected_object_name = f"{blog.author}"
        self.assertEquals(expected_object_name, "ABC")

    def test_blog_body(self):
        blog = Blog.objects.get(id=1)
        expected_object_name = f"{blog.body}"
        self.assertEquals(expected_object_name, '{"key":"value"}')

    def test_blog_cover(self):
        blog = Blog.objects.get(id=1)
        blog.update_blog_cover_url()
        blog.refresh_from_db()
        expected_object_name = f"{blog.cover.url}"
        self.assertEquals(expected_object_name, blog.cover_url)


@common_settings
class WorkshopTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Workshop.objects.create(
            title="first workshop",
            description="workshop description here",
            event_date="2019-09-25 06:00:00+00:00",
            venue="XYZ",
            cover=File(open(DUMMY_PATH, "rb")),
        )

    def test_workshop_title(self):
        workshop = Workshop.objects.get(id=1)
        expected_object_name = f"{workshop.title}"
        self.assertEquals(expected_object_name, "first workshop")

    def test_workshop_description(self):
        workshop = Workshop.objects.get(id=1)
        expected_object_name = f"{workshop.description}"
        self.assertEquals(expected_object_name, "workshop description here")

    def test_workshop_event_date(self):
        workshop = Workshop.objects.get(id=1)
        expected_object_name = f"{workshop.event_date}"
        self.assertEquals(expected_object_name, "2019-09-25 06:00:00+00:00")

    def test_workshop_venue(self):
        workshop = Workshop.objects.get(id=1)
        expected_object_name = f"{workshop.venue}"
        self.assertEquals(expected_object_name, "XYZ")

    def test_workshop_cover(self):
        workshop = Workshop.objects.get(id=1)
        workshop.update_workshop_cover_url()
        workshop.refresh_from_db()
        expected_object_name = f"{workshop.cover.url}"
        self.assertEquals(expected_object_name, workshop.cover_url)


@common_settings
class GalleryTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Gallery.objects.create(
            event="abc event",
            date="2019-09-25",
            sub_event="xyz event",
            image=File(open(DUMMY_PATH, "rb")),
        )

    def test_gallery_event(self):
        gallery = Gallery.objects.get(id=1)
        expected_object_name = f"{gallery.event}"
        self.assertEquals(expected_object_name, "abc event")

    def test_gallery_sub_event(self):
        gallery = Gallery.objects.get(id=1)
        expected_object_name = f"{gallery.sub_event}"
        self.assertEquals(expected_object_name, "xyz event")

    def test_gallery_date(self):
        gallery = Gallery.objects.get(id=1)
        expected_object_name = f"{gallery.date}"
        self.assertEquals(expected_object_name, "2019-09-25")

    def test_gallery_image(self):
        gallery = Gallery.objects.get(id=1)
        gallery.update_gallery_image_url()
        gallery.refresh_from_db()
        expected_object_name = f"{gallery.image.url}"
        self.assertEquals(expected_object_name, gallery.image_url)


@common_settings
class AlumniTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Alumni.objects.create(
            name="alumni user",
            year="2017",
            company="abc company",
            github_id="https://github.com/abc",
            linkedin_id="https://www.linkedin.com/",
            profile_pic=File(open(DUMMY_PATH, "rb")),
        )

    def test_alumni_validation_error(self):
        alumni = Alumni.objects.get(id=1)
        try:
            alumni.full_clean()
        except ValidationError as e:
            self.fail(e)

        alumni.github_id = "https://test.com/tm"
        alumni.linkedin_id = "https://www.test.com/tm"
        alumni.save()
        alumni.refresh_from_db()
        self.assertRaises(ValidationError, alumni.full_clean)

    def test_alumni_title(self):
        alumni = Alumni.objects.get(id=1)
        expected_object_name = f"{alumni.name}"
        self.assertEquals(expected_object_name, "alumni user")

    def test_alumni_year(self):
        alumni = Alumni.objects.get(id=1)
        expected_object_name = f"{alumni.year}"
        self.assertEquals(expected_object_name, "2017")

    def test_alumni_company(self):
        alumni = Alumni.objects.get(id=1)
        expected_object_name = f"{alumni.company}"
        self.assertEquals(expected_object_name, "abc company")

    def test_alumni_github_id(self):
        alumni = Alumni.objects.get(id=1)
        expected_object_name = f"{alumni.github_id}"
        self.assertEquals(expected_object_name, "https://github.com/abc")

    def test_alumni_linkedin_id(self):
        alumni = Alumni.objects.get(id=1)
        expected_object_name = f"{alumni.linkedin_id}"
        self.assertEquals(expected_object_name, "https://www.linkedin.com/")

    def test_alumni_profile_pic(self):
        alumni = Alumni.objects.get(id=1)
        alumni.update_alumni_image_url()
        alumni.refresh_from_db()
        expected_object_name = f"{alumni.profile_pic.url}"
        self.assertEquals(expected_object_name, alumni.profile_pic_url)


@common_settings
class ProjectTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Project.objects.create(
            name="first project",
            description="project description here",
            year="2019-09-25",
            github_link="https://github.com/project",
            cover=File(open(DUMMY_PATH, "rb")),
        )

    def test_project_name(self):
        project = Project.objects.get(id=1)
        expected_object_name = f"{project.name}"
        self.assertEquals(expected_object_name, "first project")

    def test_project_description(self):
        project = Project.objects.get(id=1)
        expected_object_name = f"{project.description}"
        self.assertEquals(expected_object_name, "project description here")

    def test_project_year(self):
        project = Project.objects.get(id=1)
        expected_object_name = f"{project.year}"
        self.assertEquals(expected_object_name, "2019-09-25")

    def test_project_github_link(self):
        project = Project.objects.get(id=1)
        expected_object_name = f"{project.github_link}"
        self.assertEquals(expected_object_name, "https://github.com/project")

    def test_project_cover(self):
        project = Project.objects.get(id=1)
        project.update_project_cover_url()
        project.refresh_from_db()
        expected_object_name = f"{project.cover.url}"
        self.assertEquals(expected_object_name, project.cover_url)
