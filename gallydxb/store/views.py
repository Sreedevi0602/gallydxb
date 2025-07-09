from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    hero_slides = Hero.objects.all()
    brand_banner = BrandBanner.objects.first()
    brands = Brand.objects.all()
    try:
        shirts = Category.objects.get(name__iexact='shirts') 
    except Category.DoesNotExist:
        shirts = None 
    update_slides = UpdateBanner1.objects.all()
    gally_grid = GallyGrid.objects.all()
    collection1_items = Collection1.objects.all()
    try:
        tshirts = Category.objects.get(name__iexact='t-shirts') 
    except Category.DoesNotExist:
        tshirts = None 
    update2_slides = UpdateBanner2.objects.all()
    loopy_grid = LoopyGrid.objects.all()
    collection2_items = Collection2.objects.all()

    return render(request, 'home.html', {
        'hero_slides': hero_slides, 
        'brand_banner': brand_banner, 
        'brands': brands, 
        'shirts': shirts, 
        'update_slides': update_slides,
        'gally_grid': gally_grid,
        'collection1_items': collection1_items,
        'tshirts': tshirts,
        'update2_slides': update2_slides,
        'loopy_grid': loopy_grid,
        'collection2_items': collection2_items,
        })



def about(request):
    return render(request, 'about.html', {})



def products(request):
    return render(request, 'products.html', {})



def brand(request):
    return render(request, 'brand.html', {})



def category(request):
    return render(request, 'category.html', {})
