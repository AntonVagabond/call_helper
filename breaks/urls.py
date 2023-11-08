from django.urls import path, include
from rest_framework.routers import DefaultRouter

from breaks.views import dicts

router = DefaultRouter()

router.register(prefix=r'dicts/statuses/replacements',
                viewset=dicts.ReplacementStatusView,
                basename='replacement-statuses')
router.register(prefix=r'dicts/statuses/breaks',
                viewset=dicts.BreakStatusView,
                basename='breaks-statuses')
urlpatterns = [
    path('breaks/', include(router.urls))
]

