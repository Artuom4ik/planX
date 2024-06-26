from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from links.models import Link


class Collection(models.Model):
    name = models.CharField("Название", max_length=200)
    short_description = models.TextField(
        "Краткое описание",
        max_length=200,
        blank=True
    )
    created_at = models.DateTimeField(
        default=timezone.now,
        verbose_name="Дата создания"
    )
    update_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Дата изменения"
    )
    links = models.ManyToManyField(
        Link,
        related_name="collections",
        verbose_name="Ссылки"
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="collections"
    )

    def __str__(self):
        return self.name
