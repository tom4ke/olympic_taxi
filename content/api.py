from .serializers import FaqSerializer, PhoneNumberSerializer, SMLinkSerializer, BackgroundImageSerializer, FeedbackSerializer
from .models import Faq, PhoneNumber, SMLink, BackgroundImage, Feedback
from rest_framework import viewsets, permissions


# Faq Viewset
class FaqViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAdminUser
    ]

    serializer_class = FaqSerializer

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy', 'create']:
            # which is permissions.IsAdminUser
            self.permission_classes = [permissions.IsAdminUser]
        elif self.action in ['list']:
            # which is permissions.AllowAny
            self.permission_classes = [permissions.AllowAny]
        return super().get_permissions()

    def get_queryset(self):
        queryset = Faq.objects.all()
        return queryset


# PhoneNumber Viewset
class PhoneNumberViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAdminUser
    ]

    serializer_class = PhoneNumberSerializer

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy', 'create']:
            # which is permissions.IsAdminUser
            self.permission_classes = [permissions.IsAdminUser]
        elif self.action in ['list']:
            # which is permissions.AllowAny
            self.permission_classes = [permissions.AllowAny]
        return super().get_permissions()

    def get_queryset(self):
        queryset = PhoneNumber.objects.all()
        return queryset


# SMLink Viewset
class SMLinkViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAdminUser
    ]

    serializer_class = SMLinkSerializer

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy', 'create']:
            # which is permissions.IsAdminUser
            self.permission_classes = [permissions.IsAdminUser]
        elif self.action in ['list']:
            # which is permissions.AllowAny
            self.permission_classes = [permissions.AllowAny]
        return super().get_permissions()

    def get_queryset(self):
        queryset = SMLink.objects.all()
        return queryset


# BackgroundImage Viewset
class BackgroundImageViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAdminUser
    ]

    serializer_class = BackgroundImageSerializer

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy', 'create']:
            # which is permissions.IsAdminUser
            self.permission_classes = [permissions.IsAdminUser]
        elif self.action in ['list']:
            # which is permissions.AllowAny
            self.permission_classes = [permissions.AllowAny]
        return super().get_permissions()

    def get_queryset(self):
        queryset = BackgroundImage.objects.all()
        return queryset


# Feedback Viewset
class FeedbackViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAdminUser
    ]

    serializer_class = FeedbackSerializer

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy', 'create']:
            # which is permissions.IsAdminUser
            self.permission_classes = [permissions.IsAdminUser]
        elif self.action in ['list']:
            # which is permissions.AllowAny
            self.permission_classes = [permissions.AllowAny]
        return super().get_permissions()

    def get_queryset(self):
        queryset = Feedback.objects.all()
        return queryset
