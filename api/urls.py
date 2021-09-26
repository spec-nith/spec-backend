from django.urls import include, path
from rest_framework import routers

from api import views
from api.serializer import AlumniViewSet, BlogViewSet, UserViewSet, WorkshopViewSet

router = routers.DefaultRouter()
router.register("team", UserViewSet)
router.register("workshop", WorkshopViewSet)
router.register("blog", BlogViewSet)
router.register("alumni", AlumniViewSet)


urlpatterns = [
    path("", views.HomeView, name="home"),
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls")),
]
