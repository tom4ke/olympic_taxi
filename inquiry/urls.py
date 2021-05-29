from rest_framework import routers
from .api import InquiryViewSet

router = routers.DefaultRouter()
router.register('api/inquiries', InquiryViewSet, 'categories')

urlpatterns = router.urls
