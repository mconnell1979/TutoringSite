from django.urls import path
from . import views

# app_name:name is what is used for the url ref
app_name = 'lessonplans'
urlpatterns = [
    path('', views.LessonIndexView.as_view(), name='LessonPlanIndex'),
    path('createview', views.LessonplanCreateView.as_view(), name='create'),
    path('create/', views.lesson_plan_create_view),
    path('<int:pk>/', views.LessonplanDetailView.as_view(), name='detail'),
    path('wordcard/<int:pk>/<str:wordtype>', views.WordCardView.as_view(), name='card'),
    path('grade', views.update_grade),
]