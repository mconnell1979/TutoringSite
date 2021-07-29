from django.urls import path
from . import views

urlpatterns = {
    path('', views.SightwordIndexView.as_view()),
    path('Index', views.SightwordIndexView.as_view()),
    # path('', views.index),
    # path('Index', views.index),
    # path('wordlist', views.wordlist),
    path('carousellist', views.carousellist),
}