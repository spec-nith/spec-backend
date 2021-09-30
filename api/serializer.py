from rest_framework import serializers, viewsets

from api.models import Alumni, Blog, Gallery, TeamModel, Workshop


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TeamModel
        fields = "__all__"
        read_only_fields = ("__all__",)


# ViewSets define the view behavior.
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TeamModel.objects.all()
    serializer_class = UserSerializer


class BlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"
        read_only_fields = ("__all__",)


# ViewSets define the view behavior.
class BlogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class WorkshopSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Workshop
        fields = "__all__"
        read_only_fields = ("__all__",)


# ViewSets define the view behavior.
class WorkshopViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Workshop.objects.all()
    serializer_class = WorkshopSerializer


class GallerySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Gallery
        fields = "__all__"
        read_only_fields = ("__all__",)


# ViewSets define the view behavior.
class GalleryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer


class AlumniSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Alumni
        fields = "__all__"
        read_only_fields = ("__all__",)


# ViewSets define the view behavior.
class AlumniViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Alumni.objects.all()
    serializer_class = AlumniSerializer
