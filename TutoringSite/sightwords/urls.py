from django.urls import path
from . import views


app_name = 'sightwords'
urlpatterns = [
    path('', views.SightwordIndexView.as_view(), name='SightwordsIndex'),
    path('SightWordSetList/<int:orig_set>', views.SightWordSetListView.as_view(), name='SetList'),
    path('<int:id>/', views.SightwordDetailView.as_view(), name='Detail'),
]