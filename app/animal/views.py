from django.contrib.auth.models import User, Group
from animal.models import Animal
from rest_framework import permissions, generics, viewsets
from rest_framework.decorators import action
from animal.serializers import UserSerializer, AnimalSerializer
from animal.permissions import IsOwnerOrReadOnly
from rest_framework import status
from rest_framework.response import Response


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

    # Explain create and perfomr_create
    # https://stackoverflow.com/questions/41094013/when-to-use-serializers-create-and-modelviewsets-perform-create
    def create(self, request, *args, **kwargs):
        print("Inside create of AnimalViewSet")
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        print("Inside perform_create of AnimalViewSet")
        serializer.save(owner=self.request.user)

    # If you only want to show a list of objects associated with this users
    # def get_queryset(self, *args, **kwargs):
    #     return Animal.objects.all().filter(owner=self.request.user)
