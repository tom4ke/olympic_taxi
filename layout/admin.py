from django.contrib import admin
from .models import *


@admin.register(Navbar)
class NavbarAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
