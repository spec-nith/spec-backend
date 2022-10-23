from django.contrib.auth.decorators import login_required
from django.urls import include
from django.urls import path
from rest_framework import routers

from api import views
from api.serializer import AlumniViewSet
from api.serializer import GalleryViewSet
from api.serializer import ProjectViewSet
from api.serializer import TeamViewSet
from api.serializer import WorkshopViewSet
from api.serializer import MemberRegistrationViewSet
from api.serializer import WorkshopRegistrationViewSet

router = routers.DefaultRouter()
router.register("team", TeamViewSet)
router.register("workshop", WorkshopViewSet)
router.register("alumni", AlumniViewSet)
router.register("gallery", GalleryViewSet)
router.register("projects", ProjectViewSet)
router.register("member-registration", MemberRegistrationViewSet)
router.register("workshop-registration", WorkshopRegistrationViewSet)


urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("gallery/", login_required(views.GalleryFormView), name="gallery"),
    path("workshop/", login_required(views.WorkshopFormView), name="workshop"),
    path("workshop/register/", views.WorkshopRegisterView.as_view(), name="workshop-register"),
    path("team/", login_required(views.TeamFormView), name="team"),
    path("alumni/", login_required(views.AlumniFormView), name="alumni"),
    path("project/", login_required(views.ProjectFormView), name="project"),
    path("member/registration/", views.MemberRegistrationFormView.as_view(), name="member_register"),
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls")),
    path("dump_data/", login_required(views.dump_data), name="dump_data"),
    path("cache/team/<int:pk>", views.TeamUpdateView, name="update_team"),
    path("cache/workshop/<int:pk>", views.WorkshopUpdateView, name="update_workshop"),
    path("cache/gallery/<int:pk>", views.GalleryUpdateView, name="update_gallery"),
    path("cache/alumni/<int:pk>", views.AlumniUpdateView, name="update_alumni"),
    path("cache/projects/<int:pk>", views.ProjectUpdateView, name="update_project"),
]
