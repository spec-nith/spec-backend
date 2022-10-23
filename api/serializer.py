from rest_framework import serializers
from rest_framework import viewsets

from api.models import Alumni
from api.models import Gallery
from api.models import Project
from api.models import TeamModel
from api.models import Workshop
from api.models import MemberRegistration
from api.models import Attendees

TEAM_FIELDS = (
    "id",
    "name",
    "title",
    "github_id",
    "linkedin_id",
    "profile_pic_url",
    "profile_pic_webp_url",
)
WORKSHOP_FIELDS = (
    "id",
    "title",
    "description",
    "venue",
    "event_date",
    "cover_url",
    "cover_webp_url",
)
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
    "profile_pic_webp_url",
)
PROJECT_FIELDS = (
    "id",
    "domain",
    "name",
    "year",
    "description",
    "github_link",
    "cover_url",
    "cover_webp_url",
)
MEMBER_REGISTRATION_FIELDS = (
    "id",
    "name",
    "email",
    "gender",
    "roll_no",
    "degree",
    "branch",
    "year",
    "phone",
    "home_state",
    "skills",
    "strength", 
    "weakness",
    "achievement",
    "application_response",
    "supporting_docs_link",
    "photograph_link",
    "sign_link",
    "acknowledgement",
)
WORKSHOP_REGISTRATION_FIELDS = (
    "id",
    "name",
    "email",
    "workshop",
)


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TeamModel
        fields = TEAM_FIELDS
        read_only_fields = TEAM_FIELDS


class TeamViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TeamModel.objects.values(*TEAM_FIELDS)
    serializer_class = TeamSerializer
    filterset_fields = TEAM_FIELDS[:-2]


class WorkshopSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Workshop
        fields = WORKSHOP_FIELDS
        read_only_fields = WORKSHOP_FIELDS


class WorkshopViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Workshop.objects.values(*WORKSHOP_FIELDS)
    serializer_class = WorkshopSerializer
    filterset_fields = WORKSHOP_FIELDS[:-2]


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
    filterset_fields = ALUMNI_FIELDS[:-2]


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = PROJECT_FIELDS
        read_only_fields = PROJECT_FIELDS


class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.values(*PROJECT_FIELDS)
    serializer_class = ProjectSerializer
    filterset_fields = PROJECT_FIELDS[:-2]


class MemberRegistrationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MemberRegistration
        fields = MEMBER_REGISTRATION_FIELDS
        # read_only_fields = MEMBER_REGISTRATION_FIELDS


class MemberRegistrationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MemberRegistration.objects.values(*MEMBER_REGISTRATION_FIELDS)
    serializer_class = MemberRegistrationSerializer
    filterset_fields = MEMBER_REGISTRATION_FIELDS[:-10]

class WorkshopRegistrationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Attendees
        fields = WORKSHOP_REGISTRATION_FIELDS
        # read_only_fields = MEMBER_REGISTRATION_FIELDS


class WorkshopRegistrationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Attendees.objects.values(*WORKSHOP_REGISTRATION_FIELDS)
    serializer_class = WorkshopRegistrationSerializer
    filterset_fields = WORKSHOP_REGISTRATION_FIELDS