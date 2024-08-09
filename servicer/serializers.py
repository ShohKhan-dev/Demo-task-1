from rest_framework import serializers
from servicer.models import Category, Service, Profile, ProfileService, Organization, OrganizationService, PortfolioImage, OrganizationReview, ProfileReview, ReviewImage

class CategorySerializer(serializers.ModelSerializer):
    category_children = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name_uz', 'name_ru', 'name_en', 'image', 'order_number', 'parent', 'category_children']

    def get_category_children(self, obj):
        children= obj.category_children.all()
        return CategorySerializer(children, many=True).data

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'name', 'category', 'image']

class ProfileServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileService
        fields = ['id', 'profile', 'service', 'price', 'duration']

class ProfileSerializer(serializers.ModelSerializer):
    # services = ProfileServiceSerializer(source='profileservice_set', many=True, read_only=True)

    class Meta:
        model = Profile
        fields = ['id', 'first_name', 'last_name', 'description', 'image', 'rating', 'organization']

class OrganizationServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationService
        fields = ['id', 'organization', 'service', 'price', 'duration']

class PortfolioImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortfolioImage
        fields = ['id', 'organization', 'image']

class OrganizationSerializer(serializers.ModelSerializer):
    # services = OrganizationServiceSerializer(source='organizationservice_set', many=True, read_only=True)
    # portfolio_images = PortfolioImageSerializer('portfolio_images', many=True, read_only=True)
    # profiles = ProfileSerializer('profiles', many=True, read_only=True)
    # rating = serializers.ReadOnlyField()

    class Meta:
        model = Organization
        fields = [
            'id', 'name_uz', 'name_ru', 'name_en', 'profile_type', 'category', 'main_image',
            'description_uz', 'description_ru', 'description_en', 'city', 'street', 'house_number',
            'landmark', 'latitude', 'longitude'
        ]


# class ReviewImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ReviewImage
#         fields = ['id', 'image']

# class OrganizationReviewSerializer(serializers.ModelSerializer):
#     # review_images = ReviewImageSerializer(many=True, read_only=True)

#     class Meta:
#         model = OrganizationReview
#         fields = ['id', 'organization', 'comment', 'rating', 'created_at']


# class ProfileReviewSerializer(serializers.ModelSerializer):
#     # review_images = ReviewImageSerializer(many=True, read_only=True)

#     class Meta:
#         model = ProfileReview
#         fields = ['id', 'profile', 'comment', 'rating', 'created_at']


