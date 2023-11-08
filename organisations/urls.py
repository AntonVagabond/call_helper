from django.urls import path, include
from rest_framework.routers import DefaultRouter

from organisations.views import dicts

router = DefaultRouter()

router.register(
    prefix=r'dicts/positions', viewset=dicts.PositionView, basename='positions'
)

urlpatterns = [
    path('organisation/', include(router.urls))
]
