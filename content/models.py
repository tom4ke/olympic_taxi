from django.db import models
from datetime import datetime


class Faq(models.Model):
    title = models.CharField(max_length=50, verbose_name="Вопрос")
    description = models.TextField(verbose_name="Ответ")
    q_date = models.DateField(default=datetime.now,
                              blank=True, verbose_name="Дата создания")
    is_published = models.BooleanField(
        default=True, verbose_name="Опубликовать")

    class Meta:
        verbose_name_plural = 'Часто задаваемые вопросы'
        verbose_name = 'Часто задаваемые вопросы'

    def __str__(self):
        return self.title


class PhoneNumber(models.Model):
    phone_number = models.CharField(
        max_length=20, verbose_name="Контактный номер")

    def __str__(self):
        return self.phone_number

    class Meta:
        verbose_name_plural = 'Контактные номера'
        verbose_name = 'Контактный номер'


class BackgroundImage(models.Model):
    image = models.ImageField(
        upload_to='images/%Y/%m/', blank=True, null=True)
    alt = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Фоновые изображения'
        verbose_name = 'Фоновое изображение'

    def __str__(self):
        return self.alt


class SMLink(models.Model):
    icon = models.ImageField(
        upload_to='icons/%Y/%m/', blank=True, null=True)
    title = models.CharField(max_length=30)
    href = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Ссылки на социальные сети'
        verbose_name = 'Ссылка на социальный сеть'

    def __str__(self):
        return self.title


class Feedback(models.Model):
    title = models.CharField(max_length=30, blank=True)
    description = models.TextField()
    photo = models.ImageField(
        upload_to='feedback/%Y/%m/', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Отзывы'
        verbose_name = 'Отзыв'
