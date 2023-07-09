from django.urls import path , include
from .views import PlanesList, PlaneDetail
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('', PlanesList.as_view(), name='planes_list'),
    path('<int:pk>/', PlaneDetail.as_view(), name='plane_detail'),
    path("api-auth/", include("rest_framework.urls")),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

]