from django.urls import path
from . import views


app_name = 'sightwords'
urlpatterns = [
    path('', views.SightWordIndexView.as_view(), name='Index'),
    path('SightWordSetList/<int:orig_set>', views.SightWordSetListView.as_view(), name='SetList'),
    path('<int:id>/', views.SightWordDetailView.as_view(), name='Detail'),
    path('SightWordSentenceList/', views.SightWordSentenceIndexView.as_view(), name='SentenceIndex'),
    path('SightWordSentenceList/Sentences/<int:pk>', views.SightWordSentenceView.as_view(), name='Sentences'),
    path('SightWordSentenceList/Sentences/words/<int:pk>', views.WordCardView.as_view(), name='SentenceSightWord'),
]