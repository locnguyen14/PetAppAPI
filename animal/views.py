from django.contrib.auth.models import User, Group
from animal.models import Animal
from rest_framework import permissions, generics, viewsets
from rest_framework.decorators import action
from animal.serializers import UserSerializer, AnimalSerializer
from animal.permissions import IsOwnerOrReadOnly


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    # If you only want to show a list of objects associated with this users
    # def get_queryset(self, *args, **kwargs):
    #     return Animal.objects.all().filter(owner=self.request.user)
