from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name = 'home'), #agar koi blank path leke aata hai to usse views k index function pr bhej do, path k anaam 'home
    path('about', views.about, name = 'about'),
    path('services', views.services, name = 'services'), # This is URL dispatcher
    path('contact', views.contact, name = 'contact'),
]