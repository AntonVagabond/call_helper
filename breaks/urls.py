from django.urls import path, include
from rest_framework.routers import DefaultRouter

from breaks.views import dicts, replacements, breaks

router = DefaultRouter()

router.register(prefix=r'replacements/(?P<pk>\d+)/schedule',
                viewset=breaks.BreakScheduleView, basename='breaks-schedule')
router.register(prefix=r'replacements', viewset=replacements.ReplacementView,
                basename='replacements')
router.register(prefix=r'dicts/statuses/replacements',
                viewset=dicts.ReplacementStatusView, basename='replacement-statuses')

urlpatterns = [
    path('breaks/replacements/<int:pk>/member/',
         replacements.MeReplacementMemberView.as_view(), name='replacement-member'),
    path('breaks/replacements/<int:pk>/break/', breaks.BreakMeView.as_view(),
         name='break-me'),

    path('breaks/', include(router.urls)),
]
