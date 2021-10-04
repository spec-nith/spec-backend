from django.contrib.auth.decorators import login_required
from django.urls import include, path
from rest_framework import routers

from api import views
from api.serializer import (
    AlumniViewSet,
    BlogViewSet,
    GalleryViewSet,
    ProjectViewSet,
    TeamViewSet,
    WorkshopViewSet,
)

router = routers.DefaultRouter()
router.register("team", TeamViewSet)
router.register("workshop", WorkshopViewSet)
router.register("blog", BlogViewSet)
router.register("alumni", AlumniViewSet)
router.register("gallery", GalleryViewSet)
router.register("projects", ProjectViewSet)


urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("gallery/", login_required(views.GalleryFormView.as_view()), name="gallery"),
    path("index_update/", views.URLUpdateView.as_view(), name="updater"),
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls")),
]
