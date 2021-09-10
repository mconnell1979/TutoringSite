from django.urls import path
from . import views

app_name = 'read_in_context'
urlpatterns = [
    path('', views.SRAPassageIndexView.as_view(), name='Index'),
    path('SRAPassage/<int:pk>', views.SRAPassageDetailView.as_view(), name='SRAPassage'),
]