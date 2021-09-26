from rest_framework import serializers, viewsets

from api.models import Alumni, Blog, TeamModel, Workshop


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TeamModel
        fields = "__all__"


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = TeamModel.objects.all()
    serializer_class = UserSerializer


class BlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"


# ViewSets define the view behavior.
class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class WorkshopSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Workshop
        fields = "__all__"


# ViewSets define the view behavior.
class WorkshopViewSet(viewsets.ModelViewSet):
    queryset = Workshop.objects.all()
    serializer_class = WorkshopSerializer


class AlumniSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Alumni
        fields = "__all__"


# ViewSets define the view behavior.
class AlumniViewSet(viewsets.ModelViewSet):
    queryset = Alumni.objects.all()
    serializer_class = AlumniSerializer
