from rest_framework import serializers
from .models import Faq, PhoneNumber, SMLink, BackgroundImage, Feedback


class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = '__all__'


class PhoneNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneNumber
        fields = '__all__'


class SMLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SMLink
        fields = '__all__'


class BackgroundImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BackgroundImage
        fields = '__all__'


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'
