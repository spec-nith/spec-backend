from rest_framework import serializers, viewsets

from api.models import Alumni, Blog, Gallery, Project, TeamModel, Workshop

TEAM_FIELDS = (
    "id",
    "name",
    "title",
    "github_id",
    "linkedin_id",
    "profile_pic_url",
)
BLOG_FIELDS = ("id", "title", "description", "body", "author", "published", "cover_url")
WORKSHOP_FIELDS = ("id", "title", "description", "venue", "event_date", "cover_url")
GALLERY_FIELDS = ("id", "event", "sub_event", "year", "image_url", "thumb_image_url")
ALUMNI_FIELDS = (
    "id",
    "name",
    "batch",
    "dual_degree",
    "company",
    "github_id",
    "linkedin_id",
    "profile_pic_url",
)
PROJECT_FIELDS = (
    "id",
    "domain",
    "name",
    "year",
    "description",
    "github_link",
    "cover_url",
)


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TeamModel
        fields = TEAM_FIELDS
        read_only_fields = TEAM_FIELDS


class TeamViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TeamModel.objects.values(*TEAM_FIELDS)
    serializer_class = TeamSerializer
    filterset_fields = TEAM_FIELDS


class BlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blog
        fields = BLOG_FIELDS
        read_only_fields = BLOG_FIELDS


class BlogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Blog.objects.values(*BLOG_FIELDS)
    serializer_class = BlogSerializer
    filterset_fields = ("id", "title", "description", "author", "published")


class WorkshopSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Workshop
        fields = WORKSHOP_FIELDS
        read_only_fields = WORKSHOP_FIELDS


class WorkshopViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Workshop.objects.values(*WORKSHOP_FIELDS)
    serializer_class = WorkshopSerializer
    filterset_fields = WORKSHOP_FIELDS[:-1]


class GallerySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Gallery
        fields = GALLERY_FIELDS
        read_only_fields = GALLERY_FIELDS


class GalleryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Gallery.objects.values(*GALLERY_FIELDS)
    serializer_class = GallerySerializer
    filterset_fields = GALLERY_FIELDS[:-2]


class AlumniSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Alumni
        fields = ALUMNI_FIELDS

    read_only_fields = ALUMNI_FIELDS


class AlumniViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Alumni.objects.values(*ALUMNI_FIELDS)
    serializer_class = AlumniSerializer
    filterset_fields = ALUMNI_FIELDS[:-1]


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = PROJECT_FIELDS
        read_only_fields = PROJECT_FIELDS


class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.values(*PROJECT_FIELDS)
    serializer_class = ProjectSerializer
    filterset_fields = PROJECT_FIELDS[:-1]
