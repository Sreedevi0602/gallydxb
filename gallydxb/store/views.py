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
    try:
        denims = Category.objects.get(name__iexact='denim') 
    except Category.DoesNotExist:
        denims = None 
    irishclub_grid = IrishclubGrid.objects.all()
    update3_slides = UpdateBanner3.objects.all()
    collection3_items = Collection3.objects.all()
    jackmiller_grid = JackmillerGrid.objects.all()

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
        'denims': denims,
        'irishclub_grid': irishclub_grid,
        'update3_slides': update3_slides,
        'collection3_items': collection3_items,
        'jackmiller_grid': jackmiller_grid,
        })



def about(request):
    hero_slides = AboutHero.objects.all()
    return render(request, 'about.html', {'hero_slides': hero_slides})



def products(request):
    products = ProductMedia.objects.all()
    hero_slides = ProductHero.objects.all()
    return render(request, 'products.html', {'products': products, 'hero_slides': hero_slides,})



def brand(request):
    return render(request, 'brand.html', {})



def category(request):
    return render(request, 'category.html', {})



def contact(request):
    hero_slides = ContactHero.objects.all()
    return render(request, 'contact.html', {'hero_slides': hero_slides})



def collab(request):
    return render(request, 'collab.html', {})