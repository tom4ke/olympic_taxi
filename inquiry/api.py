from .serializers import InquirySerializer
from .models import Inquiry
from rest_framework import viewsets, permissions


# Inquiry Viewset
class InquiryViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAdminUser
    ]

    serializer_class = InquirySerializer

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            # which is permissions.IsAdminUser
            self.permission_classes = [permissions.IsAdminUser]
        elif self.action in ['list', 'create']:
            # which is permissions.AllowAny
            self.permission_classes = [permissions.AllowAny]
        return super().get_permissions()

    def get_queryset(self):
        queryset = Inquiry.objects.all()
        return queryset
