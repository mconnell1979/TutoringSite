from django.urls import path
from . import views


app_name = 'vv_stories'
urlpatterns = [
    path('', views.VVStoryBookIndexView.as_view(), name='BookIndex'),
    path('StoryList/<int:book>', views.VVStoryIndexView.as_view(),
         name='StoryIndex'),
    path('Story/<int:pk>/', views.StoryDetailView.as_view(), name='Detail'),
]
