from django.db import models


# Navbars
class Navbar(models.Model):
    icon = models.ImageField(
        upload_to='navbars/%Y/%m/', blank=True, null=True)
    title = models.CharField(max_length=20)
    url = models.CharField(max_length=100)
    code = models.CharField(max_length=10)

    class Meta:
        verbose_name_plural = 'Панель навигации'
        verbose_name = 'Панель навигации'

    def __str__(self):
        return self.title
