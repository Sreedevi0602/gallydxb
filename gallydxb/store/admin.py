from django.contrib import admin
from django.utils.html import format_html
from .models import *

admin.site.site_header = "Gally Admin Panel"
admin.site.site_title = "Gally Admin"
admin.site.index_title = "Welcome to Gally Admin Panel"


# Register your models here.
class HeroAdmin(admin.ModelAdmin):
    list_display = ['heading1', 'media_preview']
    readonly_fields = ['media_preview']

    def media_preview(self, obj):
        if obj.image:
            return format_html(f'<img src="{obj.image.url}" style="max-width: 300px; max-height: 200px;" />')
        elif obj.video:
            return format_html(f'''
                <video width="320" height="240" controls>
                    <source src="{obj.video.url}" type="video/mp4">
                    Your browser does not support the video tag.
                </video>
            ''')
        return "No media uploaded"

    media_preview.short_description = "Media Preview"

admin.site.register(Hero, HeroAdmin)


class BrandBannerAdmin(admin.ModelAdmin):
    list_display = ['heading1', 'media_preview']
    readonly_fields = ['media_preview']

    def media_preview(self, obj):
        if obj.image:
            return format_html(f'<img src="{obj.image.url}" style="max-width: 300px; max-height: 200px;" />')
        elif obj.video:
            return format_html(f'''
                <video width="320" height="240" controls>
                    <source src="{obj.video.url}" type="video/mp4">
                    Your browser does not support the video tag.
                </video>
            ''')
        return "No media uploaded"

    media_preview.short_description = "Media Preview"

admin.site.register(BrandBanner, BrandBannerAdmin)



class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'logo_preview']
    readonly_fields = ['logo_preview']

    def logo_preview(self, obj):
        if obj.logo:
            return format_html(f'<img src="{obj.logo.url}" style="max-height: 80px;" />')
        return "No logo uploaded"

    logo_preview.short_description = "Logo Preview"

admin.site.register(Brand, BrandAdmin)



class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'media_preview']
    readonly_fields = ['media_preview']

    def media_preview(self, obj):
        if obj.image:
            return format_html(f'<img src="{obj.image.url}" style="max-width: 300px; max-height: 200px;" />')
        elif obj.video:
            return format_html(f'''
                <video width="320" height="240" controls>
                    <source src="{obj.video.url}" type="video/mp4">
                    Your browser does not support the video tag.
                </video>
            ''')
        return "No media uploaded"

    media_preview.short_description = "Media Preview"

admin.site.register(Category, CategoryAdmin)


class UpdateBanner1Admin(admin.ModelAdmin):
    list_display = ['heading1', 'media_preview']
    readonly_fields = ['media_preview']

    def media_preview(self, obj):
        if obj.image:
            return format_html(f'<img src="{obj.image.url}" style="max-width: 300px; max-height: 200px;" />')
        elif obj.video:
            return format_html(f'''
                <video width="320" height="240" controls>
                    <source src="{obj.video.url}" type="video/mp4">
                    Your browser does not support the video tag.
                </video>
            ''')
        return "No media uploaded"

    media_preview.short_description = "Media Preview"

admin.site.register(UpdateBanner1, UpdateBanner1Admin)



class ProductMediaInline(admin.StackedInline):
    model = ProductMedia
    extra = 1
    readonly_fields = ['media_preview']
    fields = ['image', 'media_preview']

    def media_preview(self, obj):
        if obj.image:
            return format_html(f'<img src="{obj.image.url}" style="max-width: 300px; max-height: 200px;" />')
        return "No image uploaded"

    media_preview.short_description = "Image Preview"


class ProductAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'brand', 'category', 'product_media_preview']
    inlines = [ProductMediaInline]
    readonly_fields = ['product_media_preview']

    def product_media_preview(self, obj):
        previews = []
        for media in obj.media.all():
            if media.image:
                previews.append(f'<img src="{media.image.url}" style="max-width: 100px; margin-right: 5px;" />')
        return format_html(''.join(previews)) if previews else "No images uploaded"

    product_media_preview.short_description = "All Images Preview"


admin.site.register(Product, ProductAdmin)


class GallyGridAdmin(admin.ModelAdmin):
    list_display = ['media_preview']
    readonly_fields = ['media_preview']

    def media_preview(self, obj):
        if obj.image:
            return format_html(f'<img src="{obj.image.url}" style="max-width: 300px; max-height: 200px;" />')
        return "No image uploaded"

    media_preview.short_description = "Image Preview"

admin.site.register(GallyGrid, GallyGridAdmin)


class Collection1Admin(admin.ModelAdmin):
    list_display = ['name', 'description', 'media_preview']
    readonly_fields = ['media_preview']

    def media_preview(self, obj):
        previews = []
        if obj.image1:
            previews.append(f'<img src="{obj.image1.url}" style="max-width: 200px; margin-right: 10px;" />')
        if obj.image2:
            previews.append(f'<img src="{obj.image2.url}" style="max-width: 200px;" />')
        if previews:
            return format_html(''.join(previews))
        return "No images uploaded"

    media_preview.short_description = "Image Preview"

admin.site.register(Collection1, Collection1Admin)


class UpdateBanner2Admin(admin.ModelAdmin):
    list_display = ['heading1', 'media_preview']
    readonly_fields = ['media_preview']

    def media_preview(self, obj):
        if obj.image:
            return format_html(f'<img src="{obj.image.url}" style="max-width: 300px; max-height: 200px;" />')
        elif obj.video:
            return format_html(f'''
                <video width="320" height="240" controls>
                    <source src="{obj.video.url}" type="video/mp4">
                    Your browser does not support the video tag.
                </video>
            ''')
        return "No media uploaded"

    media_preview.short_description = "Media Preview"

admin.site.register(UpdateBanner2, UpdateBanner2Admin)


class LoopyGridAdmin(admin.ModelAdmin):
    list_display = ['media_preview']
    readonly_fields = ['media_preview']

    def media_preview(self, obj):
        if obj.image:
            return format_html(f'<img src="{obj.image.url}" style="max-width: 300px; max-height: 200px;" />')
        return "No image uploaded"

    media_preview.short_description = "Image Preview"

admin.site.register(LoopyGrid, LoopyGridAdmin)


class Collection2Admin(admin.ModelAdmin):
    list_display = ['name', 'description', 'media_preview']
    readonly_fields = ['media_preview']

    def media_preview(self, obj):
        previews = []
        if obj.image1:
            previews.append(f'<img src="{obj.image1.url}" style="max-width: 200px; margin-right: 10px;" />')
        if obj.image2:
            previews.append(f'<img src="{obj.image2.url}" style="max-width: 200px;" />')
        if previews:
            return format_html(''.join(previews))
        return "No images uploaded"

    media_preview.short_description = "Image Preview"

admin.site.register(Collection2, Collection2Admin)



class UpdateBanner3Admin(admin.ModelAdmin):
    list_display = ['heading1', 'media_preview']
    readonly_fields = ['media_preview']

    def media_preview(self, obj):
        if obj.image:
            return format_html(f'<img src="{obj.image.url}" style="max-width: 300px; max-height: 200px;" />')
        elif obj.video:
            return format_html(f'''
                <video width="320" height="240" controls>
                    <source src="{obj.video.url}" type="video/mp4">
                    Your browser does not support the video tag.
                </video>
            ''')
        return "No media uploaded"

    media_preview.short_description = "Media Preview"

admin.site.register(UpdateBanner3, UpdateBanner3Admin)



class IrishclubGridAdmin(admin.ModelAdmin):
    list_display = ['media_preview']
    readonly_fields = ['media_preview']

    def media_preview(self, obj):
        if obj.image:
            return format_html(f'<img src="{obj.image.url}" style="max-width: 300px; max-height: 200px;" />')
        return "No image uploaded"

    media_preview.short_description = "Image Preview"

admin.site.register(IrishclubGrid, IrishclubGridAdmin)


class Collection3Admin(admin.ModelAdmin):
    list_display = ['name', 'description', 'media_preview']
    readonly_fields = ['media_preview']

    def media_preview(self, obj):
        previews = []
        if obj.image1:
            previews.append(f'<img src="{obj.image1.url}" style="max-width: 200px; margin-right: 10px;" />')
        if obj.image2:
            previews.append(f'<img src="{obj.image2.url}" style="max-width: 200px;" />')
        if previews:
            return format_html(''.join(previews))
        return "No images uploaded"

    media_preview.short_description = "Image Preview"

admin.site.register(Collection3, Collection3Admin)



class JackmillerGridAdmin(admin.ModelAdmin):
    list_display = ['media_preview']
    readonly_fields = ['media_preview']

    def media_preview(self, obj):
        if obj.image:
            return format_html(f'<img src="{obj.image.url}" style="max-width: 300px; max-height: 200px;" />')
        return "No image uploaded"

    media_preview.short_description = "Image Preview"

admin.site.register(JackmillerGrid, JackmillerGridAdmin)


class AboutHeroAdmin(admin.ModelAdmin):
    list_display = ['heading1', 'media_preview']
    readonly_fields = ['media_preview']

    def media_preview(self, obj):
        if obj.image:
            return format_html(f'<img src="{obj.image.url}" style="max-width: 300px; max-height: 200px;" />')
        elif obj.video:
            return format_html(f'''
                <video width="320" height="240" controls>
                    <source src="{obj.video.url}" type="video/mp4">
                    Your browser does not support the video tag.
                </video>
            ''')
        return "No media uploaded"

    media_preview.short_description = "Media Preview"

admin.site.register(AboutHero, AboutHeroAdmin)
