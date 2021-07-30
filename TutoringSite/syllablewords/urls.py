from django.urls import path
from . import views
from .views import (
    CarouselView,
)
app_name='syllablewords'
urlpatterns = [
    path('', views.index),
    path('wordlist', views.wordlist),
    path('carousel_view', CarouselView.as_view()),
]