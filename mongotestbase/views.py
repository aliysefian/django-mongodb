from django.shortcuts import render

# Create your views here.
# Serializers define the API representation.
from rest_framework import serializers
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from rest_framework import status
from rest_framework.response import Response
from mongotestbase.models import CountryDetected, Entry, EntryTest, Student


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


# ViewSets define the view behavior.
class UserViewSet(ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Student.objects.all()
    serializer_class = UserSerializer
class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = "__all__"

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryDetected
        fields = "__all__"
        abstract = True


# ViewSets define the view behavior.

class EntryViewSet(ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer




    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        # {"time_stamp": "2021-8-9 0:12:57.478", "department": 1, "countries": [{"country": "OM", "CNT": 3.0, "BYTE": 3078.0}]}
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ENTSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntryTest
        fields = "__all__"


# ViewSets define the view behavior.

class EntryTestViewSet(ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = EntryTest.objects.all()
    serializer_class = ENTSerializer