from django.shortcuts import render, get_object_or_404
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
    try:
        gally = Brand.objects.get(name__iexact='gally')
    except Brand.DoesNotExist:
        gally = None
    collection1_items = Collection1.objects.all()
    try:
        tshirts = Category.objects.get(name__iexact='t-shirts') 
    except Category.DoesNotExist:
        tshirts = None 
    update2_slides = UpdateBanner2.objects.all()
    loopy_grid = LoopyGrid.objects.all()
    try:
        loopy = Brand.objects.get(name__iexact='loopy')
    except Brand.DoesNotExist:
        loopy = None
    collection2_items = Collection2.objects.all()
    try:
        denims = Category.objects.get(name__iexact='denim') 
    except Category.DoesNotExist:
        denims = None 
    irishclub_grid = IrishclubGrid.objects.all()
    try:
        irishclub = Brand.objects.get(name__iexact='Irish Club')
    except Brand.DoesNotExist:
        irishclub = None
    update3_slides = UpdateBanner3.objects.all()
    collection3_items = Collection3.objects.all()
    jackmiller_grid = JackmillerGrid.objects.all()
    try:
        jackmiller = Brand.objects.get(name__iexact='Jack Miller')
    except Brand.DoesNotExist:
        jackmiller = None
    try:
        hoodie = Category.objects.get(name__iexact='hoodie') 
    except Category.DoesNotExist:
        hoodie = None
    collection4_items = Collection4.objects.all()
    district_grid = DistrictGrid.objects.all()
    try:
        district11 = Brand.objects.get(name__iexact='District 11')
    except Brand.DoesNotExist:
        district11 = None
    stores = Store.objects.all()

    return render(request, 'home.html', {
        'hero_slides': hero_slides, 
        'brand_banner': brand_banner, 
        'brands': brands, 
        'shirts': shirts, 
        'update_slides': update_slides,
        'gally_grid': gally_grid,
        'gally': gally,
        'collection1_items': collection1_items,
        'tshirts': tshirts,
        'update2_slides': update2_slides,
        'loopy_grid': loopy_grid,
        'loopy': loopy,
        'collection2_items': collection2_items,
        'denims': denims,
        'irishclub_grid': irishclub_grid,
        'irishclub': irishclub,
        'update3_slides': update3_slides,
        'collection3_items': collection3_items,
        'jackmiller_grid': jackmiller_grid,
        'jackmiller': jackmiller,
        'hoodie': hoodie,
        'collection4_items': collection4_items,
        'district_grid': district_grid,
        'district11': district11,
        'stores': stores,
        })



def about(request):
    hero_slides = AboutHero.objects.all()
    return render(request, 'about.html', {'hero_slides': hero_slides})



def products(request):
    products = ProductMedia.objects.all()
    hero_slides = ProductHero.objects.all()
    return render(request, 'products.html', {'products': products, 'hero_slides': hero_slides,})



def brand(request, slug):
    brand = get_object_or_404(Brand, slug=slug)
    products = Product.objects.filter(brand=brand)
    return render(request, 'brand.html', {
        'brand': brand,
        'products': products
    })



def category(request,slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category)
    return render(request, 'category.html', {'category': category, 'products': products})



def contact(request):
    hero_slides = ContactHero.objects.all()
    return render(request, 'contact.html', {'hero_slides': hero_slides})



def collab(request):
    return render(request, 'collab.html', {})



def store(request):
    stores = Store.objects.all()
    return render(request, 'store.html', {'stores': stores})