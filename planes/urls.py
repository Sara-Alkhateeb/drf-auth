from django.urls import path
from .views import PlanesList, PlaneDetail

urlpatterns = [
    path('', PlanesList.as_view(), name='planes_list'),
    path('<int:pk>/', PlaneDetail.as_view(), name='plane_detail'),
]