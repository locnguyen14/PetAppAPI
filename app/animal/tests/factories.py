from collections import OrderedDict
from faker import Faker
from factory.django import DjangoModelFactory
from factory import SubFactory
from ..models import Animal
from django.contrib.auth.models import User


locales = OrderedDict([
    ('en-US', 1),
    ('en-PH', 2),
    ('ja_JP', 3),
])
fake = Faker(locales)
Faker.seed(4231)


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    first_name = fake.name()
    last_name = fake.name()
    username = fake.address()
    password = fake.ssn()
    is_staff = False
    is_superuser = False


class AnimalFactory(DjangoModelFactory):
    name = fake.name()
    weight = fake.pydecimal(left_digits=4, right_digits=2)
    height = fake.pydecimal(left_digits=4, right_digits=2)
    note = fake.address()
    animalType = fake.pyint(min_value=0, max_value=2)
    owner = SubFactory(UserFactory)

    class Meta:
        model = Animal
