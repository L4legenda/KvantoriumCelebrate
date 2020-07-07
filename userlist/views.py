from django.shortcuts import render
from rest_framework import generics
from userlist.serializers import ChildDetailSerializer
from userlist.models import Children

class ChildCreateView(generics.CreateAPIView):
    serializer_class = ChildDetailSerializer

class ChildListView(generics.ListAPIView):
    serializer_class = ChildDetailSerializer
    queryset = Children.objects.all()
