from rest_framework import serializers
from .models import Navbar


class NavbarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Navbar
        fields = '__all__'
