from rest_framework import serializers, viewsets

from api.models import Alumni, Blog, Gallery, TeamModel, Workshop

TEAM_FIELDS = ("name", "title", "github_id", "linkedin_id", "profile_pic_url")
BLOG_FIELDS = ("title", "description", "body", "author", "published", "cover_url")
WORKSHOP_FIELDS = ("title", "description", "venue", "event_date", "cover_url")
GALLERY_FIELDS = ("event", "sub_event", "date", "image_url")
ALUMNI_FIELDS = (
    "name",
    "year",
    "dual_degree",
    "company",
    "github_id",
    "linkedin_id",
    "profile_pic_url",
)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TeamModel
        fields = TEAM_FIELDS
        read_only_fields = TEAM_FIELDS


# ViewSets define the view behavior.
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TeamModel.objects.values(*TEAM_FIELDS)
    serializer_class = UserSerializer


class BlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blog
        fields = BLOG_FIELDS
        read_only_fields = BLOG_FIELDS


# ViewSets define the view behavior.
class BlogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Blog.objects.values(*BLOG_FIELDS)
    serializer_class = BlogSerializer


class WorkshopSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Workshop
        fields = WORKSHOP_FIELDS
        read_only_fields = WORKSHOP_FIELDS


# ViewSets define the view behavior.
class WorkshopViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Workshop.objects.values(*WORKSHOP_FIELDS)
    serializer_class = WorkshopSerializer


class GallerySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Gallery
        fields = GALLERY_FIELDS
        read_only_fields = GALLERY_FIELDS


# ViewSets define the view behavior.
class GalleryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Gallery.objects.values(*GALLERY_FIELDS)
    serializer_class = GallerySerializer


class AlumniSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Alumni
        fields = ALUMNI_FIELDS

    read_only_fields = ALUMNI_FIELDS


# ViewSets define the view behavior.
class AlumniViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Alumni.objects.values(*ALUMNI_FIELDS)
    serializer_class = AlumniSerializer
