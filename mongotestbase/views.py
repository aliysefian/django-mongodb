from django.shortcuts import render

# Create your views here.
# Serializers define the API representation.
from rest_framework import serializers
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from mongotestbase.models import Student


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


# ViewSets define the view behavior.
class UserViewSet(ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Student.objects.all()
    serializer_class = UserSerializer
