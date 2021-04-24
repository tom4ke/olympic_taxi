from django.db import models
from datetime import datetime


class Faq(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    q_date = models.DateField(default=datetime.now, blank=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class PhoneNumber(models.Model):
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.phone_number


class BackgroundImage(models.Model):
    image = models.ImageField(
        upload_to='images/%Y/%m/', blank=True, null=True)
    alt = models.CharField(max_length=50)

    def __str__(self):
        return self.alt


class SMLink(models.Model):
    icon = models.ImageField(
        upload_to='icons/%Y/%m/', blank=True, null=True)
    title = models.CharField(max_length=30)
    href = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Feedback(models.Model):
    title = models.CharField(max_length=30, blank=True)
    description = models.TextField()
    photo = models.ImageField(
        upload_to='feedback/%Y/%m/', blank=True, null=True)
