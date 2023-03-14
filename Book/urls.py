from .views import BookViewSet, PhotoBookViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'book', BookViewSet, basename="book")
router.register(r'photo', PhotoBookViewSet, basename="book-photo")

urlpatterns = router.urls
