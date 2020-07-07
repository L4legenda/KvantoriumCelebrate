from django.shortcuts import render
from rest_framework import generics
from usercelebrate.serializers import CelebrateDetailSerializer
from usercelebrate.models import Celebrate

class CelebrateCreateView(generics.CreateAPIView):
    serializer_class = CelebrateDetailSerializer

class CelebrateListView(generics.ListAPIView):
    serializer_class = CelebrateDetailSerializer
    queryset = Celebrate.objects.all()
