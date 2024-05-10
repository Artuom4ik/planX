from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Link(models.Model):
    LINK_TYPE = (
        ('website', 'вебсайт'),
        ('book', 'книга'),
        ('article', 'артикль'),
        ('music', 'музыка'),
        ('video', 'видео')
    )

    title = models.CharField("Заголовок страницы", max_length=100)
    short_description = models.TextField("Краткое описание", max_length=200)
    link = models.CharField("Ссылка на страницу", max_length=100)
    image = models.ImageField(null=True, default="", verbose_name="Изображение")
    link_type = models.CharField(
        max_length=100,
        choices=LINK_TYPE,
        db_index=True,
        default="website",
        verbose_name="Тип ссылки"
    )
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Дата создания")
    update_at = models.DateTimeField(null=True, blank=True, verbose_name="Дата изменения")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="links")

    class Meta:
        unique_together = ['link', 'user']

    def __str__(self):
        return f"{self.title}, {self.link_type}"
