from rest_framework import routers
from .api import NavbarViewSet

router = routers.DefaultRouter()
router.register('api/navbars', NavbarViewSet, 'navbars')

urlpatterns = router.urls
