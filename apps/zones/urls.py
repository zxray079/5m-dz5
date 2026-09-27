from rest_framework.routers import DefaultRouter

from .views import ZoneViewSet, VisitorsViewSet


router = DefaultRouter()

router.register(r'zones', ZoneViewSet, basename='zones')
router.register(r'visitors', VisitorsViewSet, basename='visitors')

urlpatterns = router.urls