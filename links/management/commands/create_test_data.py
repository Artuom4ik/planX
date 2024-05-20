import random

from django.core.management.base import BaseCommand

from links.factories import LinkFactory, UserFactory


class Command(BaseCommand):
    help = 'Создание тестовых данных для модели Link'

    def handle(self, *args, **kwargs):
        for _ in range(12):
            user = UserFactory()
            LinkFactory.create_batch(random.randint(5, 15), user=user)
        self.stdout.write(
            self.style.SUCCESS(
                'Тестовые данные успешно созданы'
            )
        )
