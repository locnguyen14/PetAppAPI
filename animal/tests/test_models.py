from django.test import TestCase

from animal.models import Animal
from animal.tests.factories import AnimalFactory


class AnimalTestCase(TestCase):
    def test_str(self):
        animal = AnimalFactory()
        self.assertEqual(str(animal), animal.name)
