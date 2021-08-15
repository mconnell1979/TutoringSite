from django.urls import path
from . import views

# app_name:name is what is used for the url ref
app_name = 'lessonplans'
urlpatterns = [
    path('', views.LessonIndexView.as_view(), name='LessonPlanIndex'),
    path('create/', views.lessonplan_create_function),
    path('<int:pk>/', views.LessonplanDetailView.as_view(), name='detail'),
    path('word_card/<int:pk>/<str:wordtype>', views.WordCardView.as_view(), name='card'),
    path('sight_words/<int:pk>/<int:lesson_id>', views.PersonalSightWordCardView.as_view(), name='sight_words'),
    path('grade', views.update_grade),
]