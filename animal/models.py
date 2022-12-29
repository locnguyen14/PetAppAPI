from django.db import models
from django.contrib.auth.models import User
import uuid


class Animal(models.Model):
    ANIMAL_TYPES = (
        (0, 'DOG'),
        (1, 'CAT'),
        (2, 'Others'),

    )
    animal_id = models.UUIDField(
        primary_key=True, db_column='id', default=uuid.uuid4)
    name = models.CharField(max_length=100)
    weight = models.DecimalField(decimal_places=2, max_digits=6)
    height = models.DecimalField(decimal_places=2, max_digits=6)
    note = models.TextField(max_length=1000)
    animalType = models.IntegerField(choices=ANIMAL_TYPES)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='animals')

    def save(self, *args, **kwargs):
        super().save(*args, kwargs)
