from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('about/', views.about, name= 'about'),
    path('products/', views.products, name= 'products'),
    path('brand/<str:brnd>/', views.brand, name= 'brand'),
    path('category/<str:cat>/', views.category, name= 'category'),
    path('contact/', views.contact, name= 'contact'),
    path('collaborations/', views.collab, name= 'collab'),
]