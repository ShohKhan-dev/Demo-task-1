# views.py
from rest_framework import viewsets
from servicer.models import Category, Service, Profile, Organization, PortfolioImage, OrganizationService, ProfileService
from servicer.serializers import (
    CategorySerializer, 
    ServiceSerializer, 
    ProfileSerializer, 
    OrganizationSerializer, 
    PortfolioImageSerializer, 
    OrganizationServiceSerializer, 
    ProfileServiceSerializer
)
from rest_framework.response import Response
from rest_framework.decorators import action


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @action(detail=True, methods=['get'])
    def organizations(self, request, pk=None):
        category = self.get_object()
        organizations = Organization.objects.filter(category=category)
        serializer = OrganizationSerializer(organizations, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['get'])
    def services(self, request, pk=None):
        category = self.get_object()
        services = Service.objects.filter(category=category)
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    @action(detail=True, methods=['get'])
    def organizations(self, request, pk=None):
        service = self.get_object()
        organizations = OrganizationService.objects.filter(service=service)
        serializer = OrganizationServiceSerializer(organizations, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['get'])
    def profiles(self, request, pk=None):
        service = self.get_object()
        profiles = ProfileService.objects.filter(service=service)
        serializer = ProfileServiceSerializer(profiles, many=True)
        return Response(serializer.data)

class ProfileServiceViewSet(viewsets.ModelViewSet):
    queryset = ProfileService.objects.all()
    serializer_class = ProfileServiceSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    @action(detail=True, methods=['get'])
    def services(self, request, pk=None):
        profile = self.get_object()
        services = ProfileService.objects.filter(profile=profile)
        serializer = ProfileServiceSerializer(services, many=True)
        return Response(serializer.data)

class OrganizationServiceViewSet(viewsets.ModelViewSet):
    queryset = OrganizationService.objects.all()
    serializer_class = OrganizationServiceSerializer

class PortfolioImageViewSet(viewsets.ModelViewSet):
    queryset = PortfolioImage.objects.all()
    serializer_class = PortfolioImageSerializer

class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    
    @action(detail=True, methods=['get'])
    def profiles(self, request, pk=None):
        organization = self.get_object()
        profiles = Profile.objects.filter(organization=organization)
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['get'])
    def portfolio_images(self, request, pk=None):
        organization = self.get_object()
        portfolio_images = PortfolioImage.objects.filter(organization=organization)
        serializer = PortfolioImageSerializer(portfolio_images, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def services(self, request, pk=None):
        organization = self.get_object()
        services = OrganizationService.objects.filter(organization=organization)
        serializer = OrganizationServiceSerializer(services, many=True)
        return Response(serializer.data)
    




# class OrganizationReviewViewSet(viewsets.ModelViewSet):
#     queryset = OrganizationReview.objects.all()
#     serializer_class = OrganizationReviewSerializer



# class ProfileReviewViewSet(viewsets.ModelViewSet):
#     queryset = ProfileReview.objects.all()
#     serializer_class = ProfileReviewSerializer