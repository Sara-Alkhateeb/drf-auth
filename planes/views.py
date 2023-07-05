from django.shortcuts import render
from rest_framework import generics
from .models import Plane
from .serializers import PlaneSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from .permissions import IsOwnerOrReadOnly
# Create your views here.

# ListAPIView
class PlanesList(generics.ListCreateAPIView):
    queryset = Plane.objects.all()
    serializer_class = PlaneSerializer
    permission_classes = [IsAuthenticated]

# RetrieveAPIView RetrieveUpdateAPIView
class PlaneDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Plane.objects.all()
    serializer_class = PlaneSerializer
    permission_classes = [IsOwnerOrReadOnly]
