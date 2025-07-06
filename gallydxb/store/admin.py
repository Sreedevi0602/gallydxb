from django.contrib import admin
from django.utils.html import format_html
from .models import *

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