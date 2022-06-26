from django.urls import path
from . import views


app_name = 'vv_pictures'
urlpatterns = [
    path('', views.VVPictureBookIndexView.as_view(), name='BookIndex'),
    path('PictureList/<int:book>', views.VVPictureIndexView.as_view(),
         name='PictureIndex'),
    path('Story/<int:pk>/', views.PictureDetailView.as_view(), name='Detail'),
]
