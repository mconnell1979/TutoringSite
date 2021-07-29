from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('wordlist', views.wordlist),
    path('carousellist', views.carousellist),
]