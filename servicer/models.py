from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from PIL import Image
import uuid
from django.utils.deconstruct import deconstructible
import os
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator


@deconstructible
class PathAndRename:
    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        filename = '{}.{}'.format(uuid.uuid4().hex, ext)
        return os.path.join(self.path, filename)
    

class Category(MPTTModel):
    name_uz = models.CharField(max_length=255, unique=True)
    name_ru = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    image = models.ImageField(upload_to=PathAndRename('category/'))
    order_number = models.IntegerField()
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='category_children')

    class MPTTMeta:
        order_insertion_by = ['order_number']

    def __str__(self):
        return self.name_uz
    

    def save(self, *args, **kwargs):

        if self.order_number is None:
            self.order_number = siblings.count() + 1
        else:
            existing_category = Category.objects.filter(parent=self.parent, order_number=self.order_number).exclude(pk=self.pk).first()
            if existing_category:
                existing_category.order_number, self.order_number = self.order_number, existing_category.order_number
                existing_category.save()


        super().save(*args, **kwargs)

        siblings = Category.objects.filter(parent=self.parent).order_by('order_number')
        for i, sibling in enumerate(siblings, start=1):
            if sibling.order_number != i:
                sibling.order_number = i
                sibling.save()

        if self.image:
            img = Image.open(self.image.path)
            if img.height > 800 or img.width > 800:
                output_size = (800, 800)
                img.thumbnail(output_size)
                img.save(self.image.path)

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        siblings = Category.objects.filter(parent=self.parent).order_by('order_number')
        for i, sibling in enumerate(siblings, start=1):
            sibling.order_number = i
            sibling.save()
    
    # def save(self, *args, **kwargs):
    #     if self.order_number is None:
    #         siblings = Category.objects.filter(parent=self.parent)
    #         self.order_number = siblings.count() + 1
    #     super().save(*args, **kwargs)
    #     if self.image:
    #         img = Image.open(self.image.path)
    #         if img.height > 800 or img.width > 800:
    #             output_size = (800, 800)
    #             img.thumbnail(output_size)
    #             img.save(self.image.path)

class Service(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name='services', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=PathAndRename('service/'), null=True, blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            img = Image.open(self.image.path)
            if img.height > 800 or img.width > 800:
                output_size = (800, 800)
                img.thumbnail(output_size)
                img.save(self.image.path)

class Organization(models.Model):
    PROFILE_TYPE_CHOICES = [
        ('company', 'Company'),
        ('specialist', 'Specialist'),
    ]

    CITY_CHOICES = [
        ('TASHKENT', 'Tashkent'),
        ('ANDIJON', 'Andijon'),
        ('SAMARQAND', 'Samarqand'),
    ]

    name_uz = models.CharField(max_length=255)
    name_ru = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    profile_type = models.CharField(max_length=20, choices=PROFILE_TYPE_CHOICES)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    main_image = models.ImageField(upload_to=PathAndRename('organization_images/'), null=True, blank=True)
    description_uz = models.TextField()
    description_ru = models.TextField()
    description_en = models.TextField()
    city = models.CharField(max_length=255, choices=CITY_CHOICES)
    street = models.CharField(max_length=255)
    house_number = models.CharField(max_length=255)
    landmark = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)
    

    def __str__(self):
        return self.name_uz

    # @property
    # def rating(self): # 6 sections, average + up to 3 images. get average from all reviews.
    #     reviews = self.reviews.all()
    #     if reviews:
    #         return sum(review.rating for review in reviews) / reviews.count()
    #     return 0
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.main_image:
            img = Image.open(self.main_image.path)
            if img.height > 800 or img.width > 800:
                output_size = (800, 800)
                img.thumbnail(output_size)
                img.save(self.main_image.path)


class Profile(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to=PathAndRename('profile/'), null=True, blank=True)
    rating = models.PositiveIntegerField(default=0)
    organization = models.ForeignKey(Organization, related_name='profiles', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    # @property
    # def rating(self):
    #     reviews = self.reviews.all()
    #     if reviews:
    #         return sum(review.rating for review in reviews) / reviews.count()
    #     return 0
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            img = Image.open(self.image.path)
            if img.height > 800 or img.width > 800:
                output_size = (800, 800)
                img.thumbnail(output_size)
                img.save(self.image.path)

class ProfileService(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.DurationField()


class OrganizationService(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.DurationField()


class PortfolioImage(models.Model):
    organization = models.ForeignKey(Organization, related_name='portfolio_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=PathAndRename('organization_portfolio/'), blank=True, null=True)

    class Meta:
        unique_together = ['organization', 'image']

    def save(self, *args, **kwargs):
        if self.organization.portfolio_images.count() >= 10:
            raise ValidationError("An organization cannot have more than 10 portfolio images.")
        super().save(*args, **kwargs)
        if self.image:
            img = Image.open(self.image.path)
            if img.height > 800 or img.width > 800:
                output_size = (800, 800)
                img.thumbnail(output_size)
                img.save(self.image.path)



# class Review(models.Model):
#     comment = models.TextField()
#     rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
#     organization = models.ForeignKey(Organization, related_name='organization_reviews', on_delete=models.CASCADE, null=True, blank=True)
#     profile = models.ForeignKey(Profile, related_name='profile_reviews', on_delete=models.CASCADE, null=True, blank=True)

#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Review for {self.organization or self.profile}"

#     def clean(self):
#         if not self.organization and not self.profile:
#             raise ValidationError("A review must be associated with either an organization or a profile.")
#         if self.organization and self.profile:
#             raise ValidationError("A review cannot be associated with both an organization and a profile.")

#     def save(self, *args, **kwargs):
#         self.clean()
#         super().save(*args, **kwargs)



# class ReviewImage(models.Model):
#     review = models.ForeignKey(Review, related_name='review_images', on_delete=models.CASCADE)
#     image = models.ImageField(upload_to=PathAndRename('review_images/'), blank=True, null=True)

#     class Meta:
#         unique_together = ['review', 'image']

#     def save(self, *args, **kwargs):
#         if self.review.review_images.count() >= 3:
#             raise ValidationError("An organization cannot have more than 10 portfolio images.")
#         super().save(*args, **kwargs)
#         if self.image:
#             img = Image.open(self.image.path)
#             if img.height > 800 or img.width > 800:
#                 output_size = (800, 800)
#                 img.thumbnail(output_size)
#                 img.save(self.image.path)