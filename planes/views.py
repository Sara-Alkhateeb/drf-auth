from django.shortcuts import render
from rest_framework import generics
from .models import Plane
from .serializers import PlaneSerializer

# Create your views here.

# ListAPIView
class PlanesList(generics.ListCreateAPIView):
    queryset = Plane.objects.all()
    serializer_class = PlaneSerializer

# RetrieveAPIView RetrieveUpdateAPIView
class PlaneDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Plane.objects.all()
    serializer_class = PlaneSerializer
