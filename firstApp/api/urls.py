from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import firstRequest
from .views import CarSpecsViewset

router = DefaultRouter()
router.register('car-specs', CarSpecsViewset, basename='car-specs')
urlpatterns = [
    path('first/', firstRequest),
    path('', include(router.urls))
]