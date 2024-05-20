import random

import factory
from factory.django import DjangoModelFactory
from django.contrib.auth.models import User

from .models import Link


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    email = factory.Faker('email')
    username = email
    password = factory.PostGenerationMethodCall('set_password', 'password123')


class LinkFactory(DjangoModelFactory):
    class Meta:
        model = Link

    title = factory.Faker('sentence', nb_words=4)
    short_description = factory.Faker('text', max_nb_chars=200)
    link = factory.Faker('url')
    link_type = factory.LazyFunction(
        lambda: random.choice(
            ['website', 'book', 'article', 'music', 'video']
        )
    )
    user = factory.SubFactory(UserFactory)
