from django.urls import path
from . import views


app_name = 'hackablesheets'
urlpatterns = [
    path('', views.HackableBookIndexView.as_view(), name='HackableBookIndex'),
    # path('SightWordSetList/<int:orig_set>', views.SightWordSetListView.as_view(), name='SetList'),
    # path('<int:id>/', views.SightwordDetailView.as_view(), name='Detail'),
]