from django.urls import path
from . import views


app_name = 'sightwords'
urlpatterns = [
    path('', views.SightwordIndexView.as_view(), name='SightwordsIndex'),
    path('sightwordSetList/<int:orig_set>', views.SightwordSetListView.as_view(), name='SetList'),
    path('<int:id>/', views.SightwordDetailView.as_view(), name='Detail'),
    path('carousellist', views.carousellist),
]