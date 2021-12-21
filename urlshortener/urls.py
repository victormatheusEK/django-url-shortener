from rest_framework.routers import DefaultRouter
from .views import ShortenerViewSet

app_name = 'urlshortener'

router = DefaultRouter()

router.register(r'', ShortenerViewSet, basename='shortener')

urlpatterns = router.urls
