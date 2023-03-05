from django.contrib.auth.models import User
from .models import Animal
from rest_framework import serializers

from utils.utils import ChoiceField


class AnimalSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    animalType = ChoiceField(choices=Animal.ANIMAL_TYPES)

    class Meta:
        model = Animal
        fields = ['animal_id', 'name', 'weight',
                  'height', 'note', 'animalType', 'owner']

    # By default when inheriting from ModelSerializer, the .create() and .update() method is included
    # However, if you want to implement more customized create or update of serializer
    # --> need to modify those 2 functions

    def create(self, validated_data):
        return Animal.objects.create(**validated_data)
