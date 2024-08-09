# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from servicer.views import (
    CategoryViewSet,
    ServiceViewSet,
    ProfileServiceViewSet,
    ProfileViewSet,
    OrganizationServiceViewSet,
    PortfolioImageViewSet,
    OrganizationViewSet
)

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'profile-services', ProfileServiceViewSet)
router.register(r'profiles', ProfileViewSet)
router.register(r'organization-services', OrganizationServiceViewSet)
router.register(r'portfolio-images', PortfolioImageViewSet)
router.register(r'organizations', OrganizationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
