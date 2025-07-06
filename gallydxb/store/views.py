from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    hero_slides = Hero.objects.all()
    brand_banner = BrandBanner.objects.first()
    brands = Brand.objects.all()
    return render(request, 'home.html', {'hero_slides': hero_slides, 'brand_banner': brand_banner, 'brands': brands})
