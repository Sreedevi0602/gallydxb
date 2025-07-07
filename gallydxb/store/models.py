from django.db import models
from django.forms import ValidationError
from .utils.validators import validate_video_file_extension

# Create your models here.
class Hero(models.Model):
    heading1 = models.CharField(max_length=100, null=True, blank=True)
    description1 = models.TextField(max_length=500, null=True, blank=True)

    image = models.ImageField(upload_to='uploads/hero/images/', blank=True, null=True)
    video = models.FileField(upload_to='uploads/hero/videos/', blank=True, null=True, validators=[validate_video_file_extension])

    def __str__(self):
        return self.heading1

    def clean(self):
        from django.core.exceptions import ValidationError
        super().clean()
        if not self.image and not self.video:
            raise ValidationError("Please upload either an image or a video.")
        if self.image and self.video:
            raise ValidationError("Upload either an image or a video, not both.")


class BrandBanner(models.Model):
    heading1 = models.CharField(max_length=100, null=True, blank=True)

    image = models.ImageField(upload_to='uploads/brandbanner/images/', blank=True, null=True)
    video = models.FileField(
        upload_to='uploads/brandbanner/videos/',
        blank=True,
        null=True,
        validators=[validate_video_file_extension]
    )

    def __str__(self):
        return self.heading1 or "Our Brands Banner"

    def clean(self):
        super().clean()
        if not self.image and not self.video:
            raise ValidationError("Please upload either an image or a video.")
        if self.image and self.video:
            raise ValidationError("Upload either an image or a video, not both.")

    def save(self, *args, **kwargs):
        if not self.pk and BrandBanner.objects.exists():
            raise ValidationError("Only one BrandBanner instance is allowed. Please delete the existing one to add a new one.")
        super().save(*args, **kwargs)


class Brand(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)

    logo = models.ImageField(upload_to='uploads/brand_logos/', blank=True, null=True)
    

    def __str__(self):
        return self.name
    


class Category(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='uploads/categories/images/', blank=True, null=True)
    video = models.FileField(
        upload_to='uploads/categories/videos/',
        blank=True,
        null=True,
        validators=[validate_video_file_extension]
    )

    def __str__(self):
        return self.name
    
    def clean(self):
        super().clean()
        if not self.image and not self.video:
            raise ValidationError("Please upload either an image or a video.")
        if self.image and self.video:
            raise ValidationError("Upload either an image or a video, not both.")

    def save(self, *args, **kwargs):
        if not self.pk and Category.objects.exists():
            raise ValidationError("Only one Category instance is allowed. Please delete the existing one to add a new one.")
        super().save(*args, **kwargs)


class UpdateBanner1(models.Model):
    heading1 = models.CharField(max_length=100, null=True, blank=True)
    description1 = models.TextField(max_length=500, null=True, blank=True)

    image = models.ImageField(upload_to='uploads/hero/images/', blank=True, null=True)
    video = models.FileField(upload_to='uploads/hero/videos/', blank=True, null=True, validators=[validate_video_file_extension])

    def __str__(self):
        return self.heading1

    def clean(self):
        from django.core.exceptions import ValidationError
        super().clean()
        if not self.image and not self.video:
            raise ValidationError("Please upload either an image or a video.")
        if self.image and self.video:
            raise ValidationError("Upload either an image or a video, not both.")
