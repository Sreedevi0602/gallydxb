import os
from django.db import models
from django.forms import ValidationError
from .utils.validators import validate_video_file_extension
from django.utils.text import slugify

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
        
    class Meta:
        verbose_name = "Hero Banner (Home Page)"
        verbose_name_plural = "Hero Banners (Home Page)"


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

    

    def clean(self):
        if not self.pk and BrandBanner.objects.exists():
            raise ValidationError("Only one Collection instance is allowed.")
        super().clean()

    class Meta:
        verbose_name = "Our Brands Display - Background Banner (Home Page)"
        verbose_name_plural = "Our Brands Display - Background Banner (Home Page)"


class Brand(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    logo = models.ImageField(upload_to='uploads/brand_logos/', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/brand_banner/', blank=True, null=True)
    

    def save(self, *args, **kwargs):
        if self.name and not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Our Brands (Add Your Brands Here)"
        verbose_name_plural = "Our Brands (Add Your Brands Here)"
    


class Category(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    image = models.ImageField(upload_to='uploads/categories/images/', blank=True, null=True)
    video = models.FileField(
        upload_to='uploads/categories/videos/',
        blank=True,
        null=True,
        validators=[validate_video_file_extension]
    )

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if self.name and not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def clean(self):
        super().clean()
        if not self.image and not self.video:
            raise ValidationError("Please upload either an image or a video.")
        if self.image and self.video:
            raise ValidationError("Upload either an image or a video, not both.")
        
    class Meta:
        verbose_name = "Category (Add Categories Here)"
        verbose_name_plural = "Categories (Add Categories Here)"


class Collections(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    image1 = models.ImageField(upload_to='uploads/collection/', blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    def clean(self):
        super().clean()
        if not self.image1 :
            raise ValidationError("Please upload either an image.")
        
    class Meta:
        verbose_name = "Collection (Add Your Collections Here)"
        verbose_name_plural = "Collections (Add Your Collections Here)"
    


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
        
    
    class Meta:
        verbose_name = "Offers/Updates-1 (Add Any Offers/Updates to display on home screen - layer 1)"
        verbose_name_plural = "Offers/Updates-1 (Add Any Offers/Updates to display on home screen - layer 1)"


class Product(models.Model):
    code = models.CharField(max_length=100, unique=True, null=True, blank=True)
    name = models.CharField(max_length=300, null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    collection = models.ForeignKey(Collections, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.code} - {self.name}"
    

    class Meta:
        verbose_name = "Products (Add Your Products Here)"
        verbose_name_plural = "Products (Add Your Products Here)"



class ProductMedia(models.Model):
    product = models.ForeignKey(Product, related_name='media', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/products/images/', blank=True, null=True)

    def clean(self):
        super().clean()
        if not self.image:
            raise ValidationError("Please upload an image.")

    def __str__(self):
        return f"Image for {self.product.name} - {self.product.name}"
    


class GallyGrid(models.Model):
    image = models.ImageField(upload_to='uploads/gally/images/', blank=True, null=True)

    def clean(self):
        super().clean()

        if not self.image:
            raise ValidationError("Please upload an image.")

        if not self.pk and GallyGrid.objects.count() >= 6:
            raise ValidationError("You can only add up to 6 images.")

    def __str__(self):
        return "New in Gally"
    

    class Meta:
        verbose_name = "**New in Gally : Home Page (Add up to 6 Images of Products in Gally Here)"
        verbose_name_plural = "**New in Gally : Home Page (Add up to 6 Images of Products in Gally Here)"
    

class Collection1(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    image1 = models.ImageField(upload_to='uploads/collection1/', blank=True, null=True)
    image2 = models.ImageField(upload_to='uploads/collection1/', blank=True, null=True)

    def clean(self):
        if not self.pk and Collection1.objects.exists():
            raise ValidationError("Only one Collection instance is allowed.")
        super().clean()

    def __str__(self):
        return f"{self.name} Collection" 
    

    class Meta:
        verbose_name = "Collection Layer 1 : Home Screen (Add a Collection Here)"
        verbose_name_plural = "Collection Layer 1 : Home Screen (Add a Collection Here)"
    

class UpdateBanner2(models.Model):
    heading1 = models.CharField(max_length=100, null=True, blank=True)
    description1 = models.TextField(max_length=500, null=True, blank=True)

    image = models.ImageField(upload_to='uploads/update_banner2/images/', blank=True, null=True)
    video = models.FileField(upload_to='uploads/update_banner2/videos/', blank=True, null=True, validators=[validate_video_file_extension])

    def __str__(self):
        return self.heading1

    def clean(self):
        from django.core.exceptions import ValidationError
        super().clean()
        if not self.image and not self.video:
            raise ValidationError("Please upload either an image or a video.")
        if self.image and self.video:
            raise ValidationError("Upload either an image or a video, not both.")
        
    
    class Meta:
        verbose_name = "Offers/Updates-2 (Add Any Offers/Updates to display on home screen - layer 2)"
        verbose_name_plural = "Offers/Updates-2 (Add Any Offers/Updates to display on home screen - layer 2)"
        

class LoopyGrid(models.Model):
    image = models.ImageField(upload_to='uploads/loopy/images/', blank=True, null=True)

    def clean(self):
        super().clean()

        if not self.image:
            raise ValidationError("Please upload an image.")

        if not self.pk and LoopyGrid.objects.count() >= 6:
            raise ValidationError("You can only add up to 6 images.")

    def __str__(self):
        return "New in Loopy"
    

    class Meta:
        verbose_name = "**New in Loopy : Home Page (Add up to 6 Images of Products in Loopy Here)"
        verbose_name_plural = "**New in Loopy : Home Page (Add up to 6 Images of Products in Loopy Here)"
    
    

class Collection2(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    image1 = models.ImageField(upload_to='uploads/collection2/', blank=True, null=True)
    image2 = models.ImageField(upload_to='uploads/collection2/', blank=True, null=True)

    def clean(self):
        if not self.pk and Collection2.objects.exists():
            raise ValidationError("Only one Collection instance is allowed.")
        super().clean()

    def __str__(self):
        return f"{self.name} Collection" 
    

    class Meta:
        verbose_name = "Collection Layer 2 : Home Screen (Add a Collection Here)"
        verbose_name_plural = "Collection Layer 2 : Home Screen (Add a Collection Here)"
    

class UpdateBanner3(models.Model):
    heading1 = models.CharField(max_length=100, null=True, blank=True)
    description1 = models.TextField(max_length=500, null=True, blank=True)

    image = models.ImageField(upload_to='uploads/update_banner3/images/', blank=True, null=True)
    video = models.FileField(upload_to='uploads/update_banner3/videos/', blank=True, null=True, validators=[validate_video_file_extension])

    def __str__(self):
        return self.heading1

    def clean(self):
        from django.core.exceptions import ValidationError
        super().clean()
        if not self.image and not self.video:
            raise ValidationError("Please upload either an image or a video.")
        if self.image and self.video:
            raise ValidationError("Upload either an image or a video, not both.")
        

    class Meta:
        verbose_name = "Offers/Updates-3 (Add Any Offers/Updates to display on home screen - layer 3)"
        verbose_name_plural = "Offers/Updates-3 (Add Any Offers/Updates to display on home screen - layer 3)"
        

class IrishclubGrid(models.Model):
    image = models.ImageField(upload_to='uploads/irishclub/images/', blank=True, null=True)

    def clean(self):
        super().clean()

        if not self.image:
            raise ValidationError("Please upload an image.")

        if not self.pk and IrishclubGrid.objects.count() >= 6:
            raise ValidationError("You can only add up to 6 images.")

    def __str__(self):
        return "New in Irish Club"
    

    class Meta:
        verbose_name = "**New in Irish Club : Home Page (Add up to 6 Images of Products in Irish Club Here)"
        verbose_name_plural = "**New in Irish Club : Home Page (Add up to 6 Images of Products in Irish Club Here)"
    


class Collection3(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    image1 = models.ImageField(upload_to='uploads/collection3/', blank=True, null=True)
    image2 = models.ImageField(upload_to='uploads/collection3/', blank=True, null=True)

    def clean(self):
        if not self.pk and Collection3.objects.exists():
            raise ValidationError("Only one Collection instance is allowed.")
        super().clean()

    def __str__(self):
        return f"{self.name} Collection" 
    

    class Meta:
        verbose_name = "Collection Layer 3 : Home Screen (Add a Collection Here)"
        verbose_name_plural = "Collection Layer 3 : Home Screen (Add a Collection Here)"
    

class JackmillerGrid(models.Model):
    image = models.ImageField(upload_to='uploads/jackmiller/images/', blank=True, null=True)

    def clean(self):
        super().clean()

        if not self.image:
            raise ValidationError("Please upload an image.")

        if not self.pk and JackmillerGrid.objects.count() >= 6:
            raise ValidationError("You can only add up to 6 images.")

    def __str__(self):
        return "New in Jack Miller"
    

    class Meta:
        verbose_name = "**New in Jack Miller : Home Page (Add up to 6 Images of Products in Jack Miller Here)"
        verbose_name_plural = "**New in Jack Miller : Home Page (Add up to 6 Images of Products in Jack Miller Here)"
    

class AboutHero(models.Model):
    heading1 = models.CharField(max_length=100, null=True, blank=True)

    image = models.ImageField(upload_to='uploads/about_hero/images/', blank=True, null=True)
    video = models.FileField(upload_to='uploads/about_hero/videos/', blank=True, null=True, validators=[validate_video_file_extension])

    def __str__(self):
        return self.heading1

    def clean(self):
        from django.core.exceptions import ValidationError
        super().clean()
        if not self.image and not self.video:
            raise ValidationError("Please upload either an image or a video.")
        if self.image and self.video:
            raise ValidationError("Upload either an image or a video, not both.")
        

    class Meta:
        verbose_name = "**About Us - Hero Image (About Us Page)"
        verbose_name_plural = "**About Us - Hero Image (About Us Page)"
        


class ContactHero(models.Model):
    heading1 = models.CharField(max_length=100, null=True, blank=True)

    image = models.ImageField(upload_to='uploads/contact_hero/images/', blank=True, null=True)
    video = models.FileField(upload_to='uploads/contact_hero/videos/', blank=True, null=True, validators=[validate_video_file_extension])

    def __str__(self):
        return self.heading1

    def clean(self):
        from django.core.exceptions import ValidationError
        super().clean()
        if not self.image and not self.video:
            raise ValidationError("Please upload either an image or a video.")
        if self.image and self.video:
            raise ValidationError("Upload either an image or a video, not both.")
        

    class Meta:
        verbose_name = "**Contact Us - Hero Image (Contact Us Page)"
        verbose_name_plural = "**Contact Us - Hero Image (Contact Us Page)"
        

class ProductHero(models.Model):
    heading1 = models.CharField(max_length=100, null=True, blank=True)

    image = models.ImageField(upload_to='uploads/product_hero/images/', blank=True, null=True)
    video = models.FileField(upload_to='uploads/product_hero/videos/', blank=True, null=True, validators=[validate_video_file_extension])

    def __str__(self):
        return self.heading1

    def clean(self):
        from django.core.exceptions import ValidationError
        super().clean()
        if not self.image and not self.video:
            raise ValidationError("Please upload either an image or a video.")
        if self.image and self.video:
            raise ValidationError("Upload either an image or a video, not both.")
        

    class Meta:
        verbose_name = "**Products - Hero Image (Products Page)"
        verbose_name_plural = "**Products - Hero Image (Products Page)"
        

class Collection4(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    image1 = models.ImageField(upload_to='uploads/collection4/', blank=True, null=True)
    image2 = models.ImageField(upload_to='uploads/collection4/', blank=True, null=True)

    def clean(self):
        if not self.pk and Collection4.objects.exists():
            raise ValidationError("Only one Collection instance is allowed.")
        super().clean()

    def __str__(self):
        return f"{self.name} Collection" 
    

    class Meta:
        verbose_name = "Collection Layer 4 : Home Screen (Add a Collection Here)"
        verbose_name_plural = "Collection Layer 4 : Home Screen (Add a Collection Here)"
        

class DistrictGrid(models.Model):
    image = models.ImageField(upload_to='uploads/district_11/images/', blank=True, null=True)

    def clean(self):
        super().clean()

        if not self.image:
            raise ValidationError("Please upload an image.")

        if not self.pk and DistrictGrid.objects.count() >= 6:
            raise ValidationError("You can only add up to 6 images.")

    def __str__(self):
        return "New in District 11"
    

    class Meta:
        verbose_name = "**New in District 11 : Home Page (Add up to 6 Images of Products in District 11 Here)"
        verbose_name_plural = "**New in District 11 : Home Page (Add up to 6 Images of Products in District 11 Here)"
    


class Store(models.Model):
    location = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='uploads/store/images/', blank=True, null=True)
    video = models.FileField(upload_to='uploads/store/videos/', blank=True, null=True, validators=[validate_video_file_extension])

    def __str__(self):
        return self.location

    def clean(self):
        from django.core.exceptions import ValidationError
        super().clean()
        if not self.image and not self.video:
            raise ValidationError("Please upload either an image or a video.")
        if self.image and self.video:
            raise ValidationError("Upload either an image or a video, not both.")
        
    class Meta:
        verbose_name = "Store Locations : Home Screen (Add Your Store Details)"
        verbose_name_plural = "Store Locations : Home Screen (Add Your Store Details)"
    


class StoreHero(models.Model):
    heading1 = models.CharField(max_length=100, null=True, blank=True)

    image = models.ImageField(upload_to='uploads/store_hero/images/', blank=True, null=True)
    video = models.FileField(upload_to='uploads/store_hero/videos/', blank=True, null=True, validators=[validate_video_file_extension])

    def __str__(self):
        return self.heading1

    def clean(self):
        from django.core.exceptions import ValidationError
        super().clean()
        if not self.image and not self.video:
            raise ValidationError("Please upload either an image or a video.")
        if self.image and self.video:
            raise ValidationError("Upload either an image or a video, not both.")
        

    class Meta:
        verbose_name = "**Our Stores - Hero Image (Our Stores Page)"
        verbose_name_plural = "**Our Stores - Hero Image (Our Stores Page)"
        


class CollabHero(models.Model):
    heading1 = models.CharField(max_length=100, null=True, blank=True)

    image = models.ImageField(upload_to='uploads/collab_hero/images/', blank=True, null=True)
    video = models.FileField(upload_to='uploads/collab_hero/videos/', blank=True, null=True, validators=[validate_video_file_extension])

    def __str__(self):
        return self.heading1

    def clean(self):
        from django.core.exceptions import ValidationError
        super().clean()
        if not self.image and not self.video:
            raise ValidationError("Please upload either an image or a video.")
        if self.image and self.video:
            raise ValidationError("Upload either an image or a video, not both.")
        

    class Meta:
        verbose_name = "**Collaborations - Hero Image (Collaborations Page)"
        verbose_name_plural = "**Collaborations - Hero Image (Collaborations Page)"


class Collab(models.Model):
    heading1 = models.CharField(max_length=200, null=True, blank=True)
    description1 = models.TextField(max_length=1000, null=True, blank=True)

    image1 = models.ImageField(upload_to='uploads/collab/', null=True, blank=True)
    image2 = models.ImageField(upload_to='uploads/collab/', null=True, blank=True)
    image3 = models.ImageField(upload_to='uploads/collab/', null=True, blank=True)
    image4 = models.ImageField(upload_to='uploads/collab/', null=True, blank=True)
    image5 = models.ImageField(upload_to='uploads/collab/', null=True, blank=True)
    image6 = models.ImageField(upload_to='uploads/collab/', null=True, blank=True)
    image7 = models.ImageField(upload_to='uploads/collab/', null=True, blank=True)
    image8 = models.ImageField(upload_to='uploads/collab/', null=True, blank=True)
    image9 = models.ImageField(upload_to='uploads/collab/', null=True, blank=True)
    image10 = models.ImageField(upload_to='uploads/collab/', null=True, blank=True)

    def images(self):
        """Return a list of uploaded image fields (non-empty only)."""
        return [getattr(self, f'image{i}') for i in range(1, 11) if getattr(self, f'image{i}')]

    def __str__(self):
        return self.heading1 or "Untitled Collaboration"
    

    class Meta:
        verbose_name = "Collaborations Media (Add up to 10 images for each collaboration)"
        verbose_name_plural = "Collaborations Media (Add up to 10 images for each collaboration)"







