from rest_framework import routers
from .viewsets import ProductViewSet

router = routers.DefaultRouter()
router.register('products', ProductViewSet, basename='products')

urlpatterns = router.urls
