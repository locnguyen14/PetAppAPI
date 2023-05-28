# Need to reimport the new user class?
from django.contrib.auth.models import User, Group

from animal.models import Animal
from rest_framework import permissions, generics, viewsets
from rest_framework.decorators import action
from animal.serializers import AnimalSerializer
from animal.permissions import IsOwnerOrReadOnly
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from utils.utils import upload_base64_image_to_s3, generate_image_file_name, generate_image_url


class AnimalViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    serializer_class = AnimalSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    # Explain create and perfomr_create
    # https://stackoverflow.com/questions/41094013/when-to-use-serializers-create-and-modelviewsets-perform-create
    def create(self, request, *args, **kwargs):
        # Upload image
        base64_image = request.data.get("image", None)
        file_name = generate_image_file_name()
        image_url = generate_image_url(file_name) if upload_base64_image_to_s3(
            base64_image=base64_image, file_name=file_name) else ''  # Get the URL for image
        # Modify the request.data to take the image as the new url
        request.data.update({"image": image_url})

        # Do the normal things
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    # If you only want to show a list of objects associated with this users

    def get_queryset(self, *args, **kwargs):
        return self.request.user.animals.all()
