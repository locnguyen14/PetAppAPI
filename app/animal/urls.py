from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AnimalViewSet, UserViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter(trailing_slash=False)
router.register(r'animals', AnimalViewSet, basename="animal")
router.register(r'users', UserViewSet, basename="user")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
