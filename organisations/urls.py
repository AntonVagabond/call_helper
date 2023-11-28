from django.urls import path, include
from rest_framework.routers import DefaultRouter

from organisations.views import (
    dicts, organisations, employees, offers, members, groups
)

router = DefaultRouter()

router.register(prefix=r'dicts/positions', viewset=dicts.PositionView,
                basename='positions')
router.register(prefix=r'search', viewset=organisations.OrganisationSearchView,
                basename='organisations-search')
router.register(prefix=r'(?P<pk>\d+)/employees', viewset=employees.EmployeeView,
                basename='employees')
router.register(prefix=r'offers', viewset=offers.OfferUserView,
                basename='user-offers')
router.register(prefix=r'(?P<pk>\d+)/offers', viewset=offers.OfferOrganisationView,
                basename='org-offers')
router.register(prefix=r'groups/(?P<pk>\d+)/members', viewset=members.MemberView,
                basename='members')
router.register(prefix=r'groups', viewset=groups.GroupView, basename='groups')
router.register(prefix=r'', viewset=organisations.OrganisationView,
                basename='organisations')

urlpatterns = [
    path('organisations/', include(router.urls)),
]
