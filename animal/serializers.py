from django.contrib.auth.models import User
from .models import Animal
from rest_framework import serializers

from utils.utils import ChoiceField


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'animals']


class AnimalSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    animalType = ChoiceField(choices=Animal.ANIMAL_TYPES)

    class Meta:
        model = Animal
        fields = ['animal_id', 'name', 'weight',
                  'height', 'note', 'animalType', 'owner']
