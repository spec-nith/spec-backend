from django.urls import include, path
from rest_framework import routers

from api import views
from api.serializer import UserViewSet

router = routers.DefaultRouter()
router.register(r"team", UserViewSet)


urlpatterns = [
    path("", views.HomeView, name="home"),
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls")),
]
