from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Categories'
        verbose_name = 'Category'

    def __str__(self):
        return self.title


class Inquiry(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.DO_NOTHING, null=True, blank=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    phone_number = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = 'Inquiries'
        verbose_name = 'Inquiry'

    def __str__(self):
        return self.first_name + ' - ' + self.phone_number
