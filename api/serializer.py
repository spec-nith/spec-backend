from rest_framework import serializers, viewsets

from api.models import TeamModel


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TeamModel
        fields = ["name", "post"]


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = TeamModel.objects.all()
    serializer_class = UserSerializer
