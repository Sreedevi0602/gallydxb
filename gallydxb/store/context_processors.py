from .models import Brand, Category

def brand_and_category_context(request):
    return {
        'brands': Brand.objects.all(),
        'categories': Category.objects.all(),
    }
