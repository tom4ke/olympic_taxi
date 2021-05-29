from rest_framework import routers
from .api import FaqViewSet, PhoneNumberViewSet, SMLinkViewSet, BackgroundImageViewSet, FeedbackViewSet

router = routers.DefaultRouter()
router.register('api/faqs', FaqViewSet, 'faqs')
router.register('api/phone-numbers', PhoneNumberViewSet, 'phone-numbers')
router.register('api/sm-links', SMLinkViewSet, 'sm-links')
router.register('api/background-images',
                BackgroundImageViewSet, 'background-images')
router.register('api/feedbacks', FeedbackViewSet, 'feedbacks')

urlpatterns = router.urls
