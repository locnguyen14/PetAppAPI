from django.urls import path
from .views import UserDetailAPI, RegisterUserAPIView, LoginAPI

urlpatterns = [
    path('user/get-details', UserDetailAPI.as_view()),
    path('user/register', RegisterUserAPIView.as_view()),
    path('user/login', LoginAPI.as_view()),
]
