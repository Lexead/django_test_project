from django.urls import include, re_path
from rest_framework.routers import DefaultRouter

from links.views import CollectionView, LinkView

router = DefaultRouter()
router.register(r"links", LinkView, basename="links")
router.register(r"collections", CollectionView, basename="collections")

urlpatterns = [
    re_path(r"^", include(router.urls)),
]
