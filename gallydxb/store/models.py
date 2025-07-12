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


class Product(models.Model):
    code = models.CharField(max_length=100, unique=True, null=True, blank=True)
    name = models.CharField(max_length=300, null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.code} - {self.name}"



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

